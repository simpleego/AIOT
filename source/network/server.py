import socket

with socket.socket(socket.AF_INET,
                   socket.SOCK_STREAM) as s:
    s.bind(('192.168.0.27',9999))
    s.listen()
    print("서버가 시작되었습니다. 연결해 주세요...")

    conn, addr = s.accept()
    print(conn, addr)
    with conn:
        print(f"연결됨: {addr}")
        while True:
            data = conn.recv(1024)
            if not data: break
            print(f"받은 데이터 : {data.decode}")
            conn.sendall(data)
            
