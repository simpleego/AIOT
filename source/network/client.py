import socket

HOST = "192.168.0.27" # 서버 IP
PORT = 9999  # 서버 포트

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    print("서버에 연결되었습니다.")

    while True:
        msg = input("보낼 메시지 입력 (종료: exit) ")
        
        if msg.lower() == "exit":
            print(" 클라이언트를 종료합니다.")
            break

        s.sendall(msg.encode())
        data = s.recv(1024)

        print(f"서버 응답 메시지 : {data.decode()}")