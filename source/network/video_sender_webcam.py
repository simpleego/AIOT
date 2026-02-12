import socket
import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import cv2
import struct
import pickle

HOST = "0.0.0.0"
PORT = 5000

class VideoSenderGUI:
    def __init__(self, root):
        self.root = root
        self.rawwoot.title("영상 송신 서버 (웹캠 / 파일 선택)")

        self.video_source = None  # "webcam" or "file"
        self.video_path = None
        self.cap = Nonea

        # ===== GUI =====
        tk.Button(root, text="📷 웹캠 선택", width=20, command=self.select_webcam).pack(pady=5)
        tk.Button(root, text="📁 영상 파일 선택", width=20, command=self.select_file).pack(pady=5)
        tk.Button(root, text="🚀 전송 시작", width=20, command=self.start_server).pack(pady=10)

        self.status_label = tk.Label(root, text="영상 소스를 선택하세요")
        self.status_label.pack(pady=5)

    def select_webcam(self):
        self.video_source = "webcam"
        self.video_path = None
        self.status_label.config(text="웹캠 선택됨")

    def select_file(self):
        path = filedialog.askopenfilename(
            filetypes=[("Video Files", "*.mp4 *.avi *.mov")]
        )
        if path:
            self.video_source = "file"
            self.video_path = path
            self.status_label.config(text=f"선택된 파일: {path}")

    def start_server(self):
        if not self.video_source:
            messagebox.showerror("Error", "웹캠 또는 영상 파일을 선택하세요")
            return

        threading.Thread(target=self.server_thread, daemon=True).start()
        self.status_label.config(text="서버 시작... 클라이언트 연결 대기")

    def server_thread(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))
        server.listen(1)

        conn, addr = server.accept()
        self.status_label.config(text=f"클라이언트 연결됨: {addr}")

        # 영상 소스 결정
        if self.video_source == "webcam":
            self.cap = cv2.VideoCapture(0)
        else:
            self.cap = cv2.VideoCapture(self.video_path)

        if not self.cap.isOpened():
            self.status_label.config(text="영상 열기 실패")
            return

        frame_count = 0

        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            data = pickle.dumps(frame)
            size = struct.pack("Q", len(data))
            conn.sendall(size + data)

            frame_count += 1
            self.status_label.config(text=f"전송 중... Frame: {frame_count}")

            cv2.waitKey(30)  # FPS 조절

        self.cap.release()
        conn.close()
        server.close()
        self.status_label.config(text="전송 완료")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoSenderGUI(root)
    root.mainloop()