import socket
import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import cv2
import struct
import pickle
import time

HOST = "0.0.0.0"
PORT = 5000

class VideoSenderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("영상 송신 서버 (Play / Pause / Stop)")

        self.video_source = None  # "webcam" or "file"
        self.video_path = None
        self.cap = None

        self.server = None
        self.conn = None

        self.running = False
        self.paused = False

        # ===== GUI =====
        tk.Button(root, text="📷 웹캠 선택", width=20, command=self.select_webcam).pack(pady=3)
        tk.Button(root, text="📁 영상 파일 선택", width=20, command=self.select_file).pack(pady=3)

        tk.Button(root, text="▶ 재생(전송 시작)", width=20, command=self.start_server).pack(pady=3)
        tk.Button(root, text="⏸ 일시정지", width=20, command=self.pause_video).pack(pady=3)
        tk.Button(root, text="⏹ 종료", width=20, command=self.stop_video).pack(pady=3)

        self.status_label = tk.Label(root, text="영상 소스를 선택하세요")
        self.status_label.pack(pady=10)

    # ===== 영상 소스 선택 =====
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

    # ===== 서버 시작 (재생) =====
    def start_server(self):
        if not self.video_source:
            messagebox.showerror("Error", "웹캠 또는 영상 파일을 선택하세요")
            return

        if not self.running:
            self.running = True
            self.paused = False
            threading.Thread(target=self.server_thread, daemon=True).start()
            self.status_label.config(text="서버 시작... 클라이언트 연결 대기")
        else:
            # pause 상태에서 재개
            self.paused = False
            self.status_label.config(text="영상 전송 재개")

    # ===== 일시정지 =====
    def pause_video(self):
        if self.running:
            self.paused = True
            self.status_label.config(text="영상 전송 일시정지")

    # ===== 종료 =====
    def stop_video(self):
        self.running = False
        self.paused = False

        if self.cap:
            self.cap.release()

        if self.conn:
            self.conn.close()

        if self.server:
            self.server.close()

        self.status_label.config(text="영상 송신 종료")

    # ===== 서버 쓰레드 =====
    def server_thread(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((HOST, PORT))
        self.server.listen(1)

        self.conn, addr = self.server.accept()
        self.status_label.config(text=f"클라이언트 연결됨: {addr}")

        # 영상 소스 설정
        if self.video_source == "webcam":
            self.cap = cv2.VideoCapture(0)
        else:
            self.cap = cv2.VideoCapture(self.video_path)

        if not self.cap.isOpened():
            self.status_label.config(text="영상 열기 실패")
            return

        frame_count = 0

        while self.running:
            if self.paused:
                time.sleep(0.1)
                continue

            ret, frame = self.cap.read()
            if not ret:
                break

            data = pickle.dumps(frame)
            size = struct.pack("Q", len(data))

            try:
                self.conn.sendall(size + data)
            except:
                break

            frame_count += 1
            self.status_label.config(text=f"전송 중... Frame: {frame_count}")

            time.sleep(0.03)  # 약 30fps

        self.stop_video()

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoSenderGUI(root)
    root.mainloop()