"""
Server Code
@author Jesus Gutierrez
@lab Multi-Threaded File Server
"""
import socket
"""
Create the socket for the client
"""
clientSocket = socket.socket()
"""
Declrate host&port
"""
host = '127.0.0.1'
port = 1233
"""
Connect to the server, try/except methods
"""
print('Loading connection ...')
try:
    clientSocket.connect((host, port))
except socket.error as error:
    print(str(error))
"""
Opens File & Receives 1024bytes
"""
reply = clientSocket.recv(1024)
"""
Client receives the data bytes and appends into a file called “received_bio_[clientid].txt”.
"""
id = str(clientSocket.getsockname()[1])
text_file = open("received_bio_[" + id +"].txt","a")
"""
While loop that keeps receiving and printing .txt
"""
while len(reply) > 0:
    reply = clientSocket.recv(1024)
    text_file.write(reply.decode())
    print(reply.decode('utf-8'))

clientSocket.close()
