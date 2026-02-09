import socket

HOSTS = [
    'www.naver.com',
    'www.python.org',
    'www.dongyang.ac.kr',
    'testname'
]

for host in HOSTS:
    try:
        hostname,aliases,address = \
        socket.gethostbyname_ex(host)

        print('hostname : ', hostname)
        print('aliases : ', aliases)
        print('address : ', address)
    except socket.error as e_msg:
        print('{}:{}'.format(host,e_msg))
        