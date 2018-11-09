'''
### socket programming
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
	data = mysock.recv(512)
	if(len(data) < 1):
		break
	print(data.decode())
mysock.close()

'''

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()

'''
import socket

# This is using HTTP 1.0 - not all servers support the oldest protocol
# Try http://data.pr4e.org/romeo.txt if your server fails.

url = input('Enter: ')
words = url.split('/')
host = words[2]

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, 80))
mysock.send(('GET '+url+' HTTP/1.0\r\n\r\n').encode())

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode(), end='')

mysock.close()
'''