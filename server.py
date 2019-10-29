import socket
import sys
import os
'''
A “server” that receives and serves client requests for 
files stored in a local directory.
'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("welcome to the server", "utf-8"))
    clientsocket.close()