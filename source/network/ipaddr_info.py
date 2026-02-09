import binascii
import ipaddress as ipa

Addresses = [
    '192.168.0.5',
    '2001:0:9d38:6abd:480:f1f:3f57:fffb'
]

for ipaddr in Addresses:
    addr = ipa.ip_address(ipaddr)
    print(f'IP address : {addr!r}')
    print(f'IP version : {addr.version}')
    print('Packed addr',binascii.hexlify(addr.packed))
    print('Integer addr',int(addr))
    print('Is private : ',addr.is_private)


