import socket

HOSTS = [
    'www.naver.com',
    'www.python.org',
    'www.dongyang.ac.kr',
    'testname'
]

for host in HOSTS:
    try:
        print('{}:{}'.format(host, socket.gethostbyname(host)))
    except socket.error as e_msg:
        print('{}:{}'.format(host,e_msg))
        