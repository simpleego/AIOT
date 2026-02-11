import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
import os

HOST = "0.0.0.0"
BUFFER_SIZE = 4096

class P2PGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("P2P Chat with Image Transfer")

        self.peers = []

        tk.Label(root, text="내 포트").grid(row=0, column=0)
        self.port_entry = tk.Entry(root)
        self.port_entry.grid(row=0, column=1)

        self.start_btn = tk.Button(root, text="서버 시작", command=self.start_server)
        self.start_btn.grid(row=0, column=2)

        tk.Label(root, text="상대 IP").grid(row=1, column=0)
        self.ip_entry = tk.Entry(root)
        self.ip_entry.grid(row=1, column=1)

        tk.Label(root, text="상대 포트").grid(row=1, column=2)
        self.peer_port_entry = tk.Entry(root)
        self.peer_port_entry.grid(row=1, column=3)

        self.connect_btn = tk.Button(root, text="피어 연결", command=self.connect_peer)
        self.connect_btn.grid(row=1, column=4)

        self.chat_area = scrolledtext.ScrolledText(root, width=60, height=20)
        self.chat_area.grid(row=2, column=0, columnspan=5)
        self.chat_area.config(state="disabled")

        self.msg_entry = tk.Entry(root, width=40)
        self.msg_entry.grid(row=3, column=0, columnspan=3)

        self.send_btn = tk.Button(root, text="전송", command=self.send_message)
        self.send_btn.grid(row=3, column=3)

        self.file_btn = tk.Button(root, text="이미지 전송", command=self.send_image)
        self.file_btn.grid(row=3, column=4)

    # ===== 서버 시작 =====
    def start_server(self):
        port = int(self.port_entry.get())
        threading.Thread(target=self.server_thread, args=(port,), daemon=True).start()
        self.log(f"[서버 시작] 포트 {port}")

    def server_thread(self, port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, port))
        server.listen()

        while True:
            conn, addr = server.accept()
            self.peers.append(conn)
            self.log(f"[연결됨] {addr}")
            threading.Thread(target=self.receive_message, args=(conn, addr), daemon=True).start()

    # ===== 피어 연결 =====
    def connect_peer(self):
        ip = self.ip_entry.get()
        port = int(self.peer_port_entry.get())

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip, port))
        self.peers.append(client)
        self.log(f"[피어 연결] {ip}:{port}")
        threading.Thread(target=self.receive_message, args=(client, (ip, port)), daemon=True).start()

    # ===== 메시지 수신 =====
    def receive_message(self, conn, addr):
        while True:
            try:
                header = conn.recv(BUFFER_SIZE).decode()

                if not header:
                    break

                if header.startswith("MSG|"):
                    msg = header.split("|", 1)[1]
                    self.log(f"[{addr}] {msg}")

                elif header.startswith("FILE|"):
                    _, filename, filesize = header.split("|")
                    filesize = int(filesize)

                    save_path = f"received_{filename}"
                    with open(save_path, "wb") as f:
                        received = 0
                        while received < filesize:
                            data = conn.recv(BUFFER_SIZE)
                            f.write(data)
                            received += len(data)

                    self.log(f"[파일 수신] {save_path}")

            except:
                break

        self.peers.remove(conn)
        conn.close()
        self.log(f"[연결 종료] {addr}")

    # ===== 텍스트 전송 =====
    def send_message(self):
        msg = self.msg_entry.get()
        if msg == "":
            return

        packet = f"MSG|{msg}".encode()
        self.log(f"[나] {msg}")

        for peer in self.peers:
            peer.send(packet)

        self.msg_entry.delete(0, tk.END)

    # ===== 이미지 전송 =====
    def send_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif")]
        )

        if not file_path:
            return

        filename = os.path.basename(file_path)
        filesize = os.path.getsize(file_path)

        header = f"FILE|{filename}|{filesize}".encode()

        for peer in self.peers:
            peer.send(header)
            with open(file_path, "rb") as f:
                while True:
                    data = f.read(BUFFER_SIZE)
                    if not data:
                        break
                    peer.send(data)

        self.log(f"[이미지 전송 완료] {filename}")

    # ===== 로그 출력 =====
    def log(self, message):
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, message + "\n")
        self.chat_area.config(state="disabled")
        self.chat_area.yview(tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = P2PGUI(root)
    root.mainloop()