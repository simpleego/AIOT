# 네트워크 기초

📄 [파이썬(PYTHON) : 중급] 네트워크 프로그래밍
👤 작성자: GDNGY 
📅 발행일: ##(1) ##(1) ##(1) 
📄 페이지 수: p##(1) ##(1) 

개요
소켓 프로그래밍, HTTP 요청 및 응답 처리, RESTful API 개념, 웹 스크레이핑 기법 등 네트워크 프로그래밍 관련 내용을 다루고 있음##(1) 소켓 프로그래밍에서는 소켓의 개념, TCP/IP, UDP 프로토콜을, HTTP 요청 및 응답 처리에서는 HTTP 프로토콜과 요청 메서드, Python에서의 HTTP 요청 및 응답 처리를 설명함##(1) RESTful API, 웹 스크레이핑에 대한 기본적인 이해와 Python에서의 구현 방법을 제공함##(1) 

# 주요 내용
##(1) 네트워크 프로그래밍  
소켓 프로그래밍을 통해 네트워크 통신을 구현하는 방법 학습, HTTP 요청 및 응답 처리, RESTful API 개념 및 활용, 웹 스크레이핑 기법을 통해 웹사이트에서 데이터를 추출하는 방법 학습 
##(1) 소켓 프로그래밍  
소켓 프로그래밍은 소켓을 통해 네트워크 통신을 구현하며, HTTP 요청 및 응답 처리, RESTful API 개념 및 활용, 웹 스크레이핑 기법을 통해 웹사이트에서 데이터를 추출하는 방법을 학습
소켓은 컴퓨터 네트워크에서 데이터를 주고받는 두 컴퓨터 간의 통신을 가능하게 하는 연결점, 서버 소켓은 특정 포트에서 연결 요청을 기다리고 클라이언트 소켓은 서버의 특정 포트로 연결을 요청 
##(1) TCP/IP 소켓 프로그래밍  
TCP/IP는 인터넷에서 가장 널리 사용되는 프로토콜, TCP는 데이터를 패킷으로 나누어 안전하게 전송, IP는 이 패킷들을 목적지로 전달, Python에서는 socket 모듈을 이용하여 TCP/IP 소켓을 쉽게 구현
TCP/IP 프로토콜을 이용하여 서버 소켓을 구현, 클라이언트로부터 데이터를 받으면, 그대로 다시 클라이언트에게 데이터를 전송하는 에코 서버 구현 
##(1) UDP 소켓 프로그래밍  
UDP는 TCP와 달리 연결 없이 데이터를 전송하는 프로토콜, 전송이 보장되지 않지만, 빠른 전송 속도, Python에서는 socket 모듈을 이용하여 UDP 소켓을 구현 
##(1) HTTP 요청 및 응답 처리  
HTTP(Hypertext Transfer Protocol)는 클라이언트와 서버 간의 데이터 전송을 위해 사용되는 프로토콜, 요청과 응답으로 구성, Python에서는 requests 라이브러리를 이용하여 HTTP 요청을 생성하고 전송
HTTP 응답에는 상태 코드가 포함, ##(1) OK, ##(1) Bad Request, ##(1) Not Found, ##(1) Internal Server Error 등 상태 코드에 따라 서버의 응답을 확인 
##(1) RESTful API 개념 및 활용  
REST(Representational State Transfer)는 웹 서비스 설계를 위한 아키텍처 스타일, HTTP를 활용, 웹의 장점을 최대한 활용, Stateless, Client-Server, Cacheable, Layered System 원칙
RESTful API는 REST 원칙에 기반, HTTP 메서드(GET, POST, PUT, DELETE 등) 활용, URI를 이용해 리소스 식별, 데이터 포맷으로 JSON 사용 
##(1) Python에서의 RESTful API 활용  
Python에서는 requests 라이브러리를 통해 RESTful API를 호출 가능, GET 요청을 보내는 예제, 응답의 내용은 response##(1)json()을 통해 JSON 형태로 확인 
##(1) 웹 스크레이핑 기법  
웹 스크레이핑이란 웹사이트에서 원하는 정보를 추출하는 기술, 웹페이지의 HTML 구조를 분석하고 필요한 데이터만 추출
BeautifulSoup는 웹페이지의 HTML을 분석하고 조작하기 위한 Python 라이브러리, Selenium은 웹 브라우저를 제어할 수 있는 자동화 도구 

## 참고 사이트
- https://gdngy##(1)tistory##(1)com/##(1)
