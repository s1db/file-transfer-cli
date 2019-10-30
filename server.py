import socket
import sys
import os
from filetransfer import *


HOST = "127.0.0.1"
PORT = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((HOST, PORT))
    s.listen(5)
except Exception as e:
	# Print the exception message
	print(e)
	# Exit with a non-zero value, to indicate an error condition
	exit(1)
print("Listening ...")

while True:
    s, addr = s.accept()
    print("[+] Client connected: ", addr)
    REQUEST_TYPE = s.recv(512).decode()
    
    if(REQUEST_TYPE=="get"):
        receive_file(s, "server")
    elif(REQUEST_TYPE=="put"):
        fileName = s.recv(1024).decode()
        print(fileName)
        send_file(s, fileName, "server")
    elif(REQUEST_TYPE=="list"):
        list_dir()
    # close connection
    s.close()
    print("[-] Client disconnected")
    sys.exit(0)