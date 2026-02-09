import socket
import threading
import random

# 임의의 메시지 목록
RESPONSES = [
    "안녕하세요!",
    "요청을 잘 받았습니다.",
    "오늘도 좋은 하루 되세요.",
    "서버에서 보낸 랜덤 메시지입니다.",
    "데이터 수신 완료!",
    "드론 통신 테스트 중입니다.",
    "응답 메시지 전송합니다."
]

def handle_client(conn, addr):
    print(f"[클라이언트 접속] {addr}")

    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                print(f"[클라이언트 종료] {addr}")
                break

            print(f"[{addr}] 받은 데이터: {data.decode()}")

            # 임의의 메시지 생성
            response = random.choice(RESPONSES)
            conn.sendall(response.encode())


def main():
    HOST = '192.168.0.27'
    PORT = 9999

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("서버가 시작되었습니다. 여러 클라이언트 접속 가능...")

        while True:
            conn, addr = s.accept()
            # 클라이언트마다 스레드 생성
            thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            thread.start()
            print(f"[활성 연결 수] {threading.active_count() - 1}")

if __name__ == "__main__":
    main()
