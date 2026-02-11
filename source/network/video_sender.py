import socket
import tkinter as tk
from tkinter import filedialog
import threading
import cv2
import struct
import pickle

HOST = "0.0.0.0"
PORT = 5000

class VideoSender:
    def __init__(self, root):
        self.root = root
        self.root.title('영상 송신 서버')

        self.video_path = None

        # 영상 파일 선택
        tk.Button(root, text="영상 파일 선택", command=self.select_video).pack(pady=5)

        # 영상 전송
        tk.Button(root, text="전송시작", command=self.start_server).pack(pady=5)

        # 서버 상태 표시
        self.status = tk.Label(root, text="대기 중...")
        self.status.pack(pady=5)

    # 영상 선택
    def select_video(self):
        self.video_path = filedialog.askopenfilename(
            filetypes=[("Video Files","*.mp4 *.avi *.mov")]
        )
        self.status.config(text=f"선택된 영상: {self.video_path}")

    # 서버 시작
    def start_server(self):
        if not self.video_path:
            return
        
        threading.Thread(target=self.server_thread, daemon=True).start()
        self.status.config(text="서버 시작됨... 연결대기")

    def server_thread(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST,PORT))
        server.listen(1)

        conn, addr = server.accept()
        self.status.config(text=f"클라이언트 연결됨...{addr}")

        cap = cv2.VideoCapture(self.video_path)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            data = pickle.dumps(frame)
            size = struct.pack("Q", len(data))

            conn.sendall(size+data)
            cv2.waitKey(10) # 프레임 속도 조절

        cap.release()
        conn.close()
        server.close()
        self.status.config(text="전송 완료")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoSender(root)
    root.mainloop()