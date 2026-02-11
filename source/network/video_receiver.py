import socket
import tkinter as tk
from PIL  import Image, ImageTk
import threading
import cv2
import struct
import pickle

SERVER_IP = "127.0.0.1"
PORT = 5000

class VideoReceiver:
    def __init__(self, root):
        self.root = root
        self.root.title('영상 수신 클라이언트')

        # 서버 정보
        tk.Label(root, text="서버 IP").pack()
        self.ip_entry = tk.Entry(root)
        self.ip_entry.pack()
        self.ip_entry.insert(0,SERVER_IP)

        # 서버 연결
        tk.Button(root, text="연결 시작", command=self.start_client).pack(pady=5)

        # 레이블 
        self.video_label = tk.Label(root)
        self.video_label.pack()
        
        self.running = False

    # 클라이언트 시작
    def start_client(self):        
        threading.Thread(target=self.client_thread, daemon=True).start()

    def client_thread(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
        client.connect((self.ip_entry.get(),PORT))

        data_buffer = b""
        payload_size = struct.calcsize("Q")

        self.running = True

        while self.running:
            while len(data_buffer) < payload_size:
                packet = client.recv(4096)
                if not packet:
                    return
                data_buffer += packet
            
            packed_size = data_buffer[:payload_size]
            data_buffer = data_buffer[payload_size:]

            frame_size = struct.unpack("Q", packed_size)[0]

            while len(data_buffer) < frame_size:
                data_buffer += client.recv(4096)
            
            frame_data = data_buffer[:frame_size]
            data_buffer = data_buffer[frame_size:]

            frame_data = pickle.loads(frame_data)
            frame = cv2.cvtColor(frame_data, cv2.COLOR_BGR2RGB)

            img = Image.fromarray(frame)
            img = img.resize((500,400))
            imgtk = ImageTk.PhotoImage(image=img)

            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)

        client.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoReceiver(root)
    root.mainloop()