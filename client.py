import socket
import sys
from filetransfer import *

HOST = "127.0.0.1"
PORT = 7213

s = socket.socket(socket.AF_INET,   socket.SOCK_STREAM)
try:
    s.connect((HOST, PORT))
except Exception as e:
	# Print the exception message
	print(e)
	# Exit with a non-zero value, to indicate an error condition
	exit(1)
print("[+] Connection Established with Server")
# close connection
receive_file(s, "client")
#send_file(s, "hot.txt", "client")
s.close()
print("[-] Disconnected")
sys.exit(0)