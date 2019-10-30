'''
TODO:
- []
'''
import socket
import sys
import os
from filetransfer import *


HOST = "127.0.0.1"
PORT = 7213

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

    send_file(s, "shit.txt", "server")
 #   receive_file(s, "server")
    # close connection
    s.close()
    print("[-] Client disconnected")
    sys.exit(0)