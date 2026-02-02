# 전체 코드

---

# 🟦 **01_socket**

---

## 📌 `tcp_server.py`

```python
import socket

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 12345))
    server_socket.listen()

    print("TCP Server started on port 12345...")

    while True:
        client_socket, addr = server_socket.accept()
        print("Connected by", addr)

        while True:
            data = client_socket.recv(1024)
            if not data:
                break

            print("Received:", data.decode())
            client_socket.sendall(data)

        client_socket.close()

if __name__ == "__main__":
    main()
```

---

## 📌 `tcp_client.py`

```python
import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    while True:
        msg = input("Message (q to quit): ")
        if msg == 'q':
            break

        client_socket.sendall(msg.encode())
        data = client_socket.recv(1024)
        print("Received:", data.decode())

    client_socket.close()

if __name__ == "__main__":
    main()
```

---

## 📌 `udp_server.py`

```python
import socket

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('', 12345))

    print("UDP Server started on port 12345...")

    while True:
        data, addr = server_socket.recvfrom(1024)
        print("Received from", addr, data.decode())
        server_socket.sendto(data, addr)

if __name__ == "__main__":
    main()
```

---

## 📌 `udp_client.py`

```python
import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        msg = input("Message (q to quit): ")
        if msg == 'q':
            break

        client_socket.sendto(msg.encode(), ('localhost', 12345))
        data, addr = client_socket.recvfrom(1024)
        print("Received:", data.decode())

    client_socket.close()

if __name__ == "__main__":
    main()
```

---

# 🟦 **02_http**

---

## 📌 `http_get.py`

```python
import requests

def main():
    response = requests.get('http://example.com')
    print("Status:", response.status_code)
    print(response.text)

if __name__ == "__main__":
    main()
```

---

## 📌 `http_post.py`

```python
import requests

def main():
    data = {'key1': 'value1', 'key2': 'value2'}
    response = requests.post('http://httpbin.org/post', data=data)

    print("Status:", response.status_code)
    print(response.text)

if __name__ == "__main__":
    main()
```

---

## 📌 `http_status_check.py`

```python
import requests

def main():
    url = input("Enter URL: ")
    response = requests.get(url)

    print("Status Code:", response.status_code)

if __name__ == "__main__":
    main()
```

---

# 🟦 **03_rest_api**

---

## 📌 `rest_get.py`

```python
import requests

def main():
    response = requests.get('https://api.github.com')
    print(response.json())

if __name__ == "__main__":
    main()
```

---

## 📌 `rest_parse_json.py`

```python
import requests

def main():
    response = requests.get('https://api.github.com')
    data = response.json()

    for key, value in data.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
```

---

## 📌 `rest_post.py`

```python
import requests

def main():
    url = "https://httpbin.org/post"
    payload = {"name": "jong", "msg": "hello"}

    response = requests.post(url, json=payload)

    print("Status:", response.status_code)
    print(response.json())

if __name__ == "__main__":
    main()
```

---

# 🟦 **04_web_scraping**

---

## 📌 `bs_basic.py`

```python
from bs4 import BeautifulSoup
import requests

def main():
    response = requests.get("https://www.example.com")
    soup = BeautifulSoup(response.text, "html.parser")

    h1 = soup.find("h1")
    print("H1 Tag:", h1.text if h1 else "Not found")

if __name__ == "__main__":
    main()
```

---

## 📌 `bs_real_site.py`

```python
from bs4 import BeautifulSoup
import requests

def main():
    url = "https://example.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    items = soup.find_all(class_="item-class-name")

    for item in items:
        print(item.text)

if __name__ == "__main__":
    main()
```

---

## 📌 `selenium_basic.py`

```python
from selenium import webdriver

def main():
    driver = webdriver.Firefox()
    driver.get("https://www.example.com")

    print("Page Title:", driver.title)

    driver.quit()

if __name__ == "__main__":
    main()
```

---

# 🎯 **jong을 위한 마무리**

이제 네트워크 실습 프로젝트의 **모든 파일이 완성된 상태**야.  
원하면:

- ZIP 파일 구조로 묶어서 제공  
- GitHub Actions CI/CD 추가  
- FastAPI 기반 REST 서버 추가  
- Docker 실행 환경 구성  

이런 것도 만들어줄 수 있어.
