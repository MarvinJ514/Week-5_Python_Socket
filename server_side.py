#Python Socket Server
#Author: Marvin Johnson
#Created: 2020-02-07
#Description: Server will listen on designated port for message being pushed
#from client. Once message is recieved server program will reply with predetermined
#reply and close session. 

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 9500
s.bind(('0.0.0.0', port))
print ('Socket binded to port 9500')
s.listen(3)
print ('Socket is listening')

while True:
    clientConnection, addr = s.accept()
    print ('Connection made')
    msg =  clientConnection.recv(1024)
    data = msg.decode("utf-8")
    print('Message recieved:', data)
    if data == 'Hello':
        reply = 'Hi'
        clientConnection.sendall(reply.encode())
        print('Reply Sent:', reply)
        break
    else:
        reply = 'Goodbye'
        clientConnection.sendall(reply.encode())
        print('Reply Sent:', reply)
        break

clientConnection.close()
                          