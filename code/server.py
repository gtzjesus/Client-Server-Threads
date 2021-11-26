"""
Server Code
@author Jesus Gutierrez
@lab Multi-Threaded File Server
"""
import socket
from _thread import *
"""
Create the socket for the server
"""
serverSocket = socket.socket()
"""
Declrate host&port
"""
host = '127.0.0.1'
port = 1233
"""
Connections implementation
"""
threads = 0
try:
    serverSocket.bind((host, port))
except socket.error as error:
    print(str(error))
print('Loading connection ...')
serverSocket.listen(5)
"""
Implement function that send info to individual client
"""
def clientThread(connection):
    """
    Open/Read File
    """
    bio_text = open("bio.txt")
    connection.send(str.encode('THIS IS THE SERVER, WELCOME.'))
    buffer = bio_text.read()
    """
    While loop to send '1024' bytes
    """ 
    while len(buffer) > 0:
        connection.send(buffer[:1024].encode())
        buffer = buffer[1024:]
    connection.close()
"""
While loop that creates a thread every execution
"""
while True:
    Client, hosting = serverSocket.accept()
    print('Connection is to: ' + hosting[0] + ':' + str(hosting[1]))
    start_new_thread(clientThread, (Client, ))
    threads += 1
    print('Thread: ' + str(threads))
serverSocket.close()