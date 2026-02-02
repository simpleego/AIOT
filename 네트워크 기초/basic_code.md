# basic_code

## ✅ **1. TCP/IP 서버 (Python)**

```python
import socket

# 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 소켓 바인드 : ''는 모든 IP에 바인드하라는 의미
server_socket.bind(('', 12345))

# 소켓이 연결 요청을 기다림
server_socket.listen()

while True:
    # 연결 수락
    client_socket, addr = server_socket.accept()
    print('Connected by', addr)

    while True:
        # 클라이언트로부터 데이터 받기
        data = client_socket.recv(1024)
        if not data:
            break

        print('Received from', addr, data.decode())

        # 받은 데이터를 클라이언트에게 다시 전송 (에코)
        client_socket.sendall(data)

    # 연결 종료
    client_socket.close()
```

---

## ✅ **2. UDP 서버 (Python)**

```python
import socket

# 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 소켓 바인드
server_socket.bind(('', 12345))

while True:
    # 클라이언트로부터 데이터 받기
    data, addr = server_socket.recvfrom(1024)
    print('Received from', addr, data.decode())

    # 받은 데이터를 클라이언트에게 다시 전송
    server_socket.sendto(data, addr)
```

---

## ✅ **3. UDP 클라이언트 (Python)**

```python
import socket

# 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("Enter message to send: ")
    if msg == 'q':
        break

    # 데이터 전송
    client_socket.sendto(msg.encode(), ('localhost', 12345))

    # 서버로부터 응답 받기
    data, addr = client_socket.recvfrom(1024)
    print('Received from', addr, data.decode())

client_socket.close()
```

---

## ✅ **4. HTTP GET 요청 (requests)**

```python
import requests

# GET 요청
response = requests.get('http://example.com')

# 응답 내용 출력
print(response.text)
```

---

## ✅ **5. HTTP POST 요청 (requests)**

```python
import requests

data = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('http://example.com', data=data)

print('Status Code:', response.status_code)
print('Response Body:', response.text)
```

---

## ✅ **6. REST API GET 요청**

```python
import requests

# RESTful API GET 요청
response = requests.get('https://api.github.com')

# 응답 출력
print(response.json())
```

---

## ✅ **7. REST API 응답 처리**

```python
import requests

response = requests.get('https://api.github.com')

data = response.json()

for key, value in data.items():
    print(f'{key}: {value}')
```

---

## ✅ **8. BeautifulSoup 기본 사용**

```python
from bs4 import BeautifulSoup
import requests

# 웹페이지 불러오기
response = requests.get('https://www.example.com')
html = response.text

# BeautifulSoup 객체 생성
soup = BeautifulSoup(html, 'html.parser')

# 태그를 이용한 데이터 추출
h1_tag = soup.find('h1')
print(h1_tag.text)
```

---

## ✅ **9. BeautifulSoup 실제 사이트 예제**

```python
from bs4 import BeautifulSoup
import requests

response = requests.get('https://real-website.com')
html = response.text

soup = BeautifulSoup(html, 'html.parser')

items = soup.find_all(class_='item-class-name')
for item in items:
    print(item.text)
```

---

## ✅ **10. Selenium 기본 사용**

```python
from selenium import webdriver

# WebDriver 객체 생성
driver = webdriver.Firefox()

# 웹사이트 접속
driver.get('https://www.example.com')

# 웹사이트 제목 출력
print(driver.title)

driver.quit()
```

---

## ✅ **11. Selenium 실제 사이트 예제**

```python
from selenium import webdriver

driver = webdriver.Firefox()

driver.get('https://real-website.com')

element = driver.find_element_by_css_selector('div.some-class')

print(element.text)

driver.quit()
```

---

# 🎯 정리 완료!

필요하면:

- 이 코드들을 **하나의 .py 파일로 묶어서 다운로드**  
- GitHub README용 마크다운 정리  
- 각 코드에 대한 설명 추가  
- 실습용 예제 프로젝트 구성  

도 만들어줄 수 있어.
