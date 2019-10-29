import socket
import sys
import os
'''
A “client” that allows the user to upload/download files 
from the server, as well as list the files currently stored
on the server side.
'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

while True:
    msg = s.recv(2)
    print(msg.decode("utf-8"))