#Python Socket Client
#Author: Marvin Johnson
#Created: 2020-02-07
#Description: Program garners input from user and sends message to server
#through socket connection. Client will recieve a reply from server and
#print to screen

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 9500
s.connect(('localhost', port))
myMessage = input('Input: ')
s.sendall(myMessage.encode())

replyMsg = s.recv(1024)
data = replyMsg.decode("utf-8")
print('Reply received:', data)

s.close()




