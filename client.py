import socket
import sys
from filetransfer import *

HOST = str(sys.argv[1])
PORT = int(sys.argv[2])
REQUEST_TYPE = str(sys.argv[3])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((HOST, PORT))
except Exception as e:
    print(e)
    exit(1)
print("[+] Established Connection with Server")
FILES_ON_SERVER = receive_listing(s, "client")
FILES_ON_CLIENT = os.listdir(r"./client")
if(REQUEST_TYPE == "get"):
    fileName = sys.argv[4]
    if(fileName in FILES_ON_SERVER):
        s.sendall("put".encode('utf-8'))
        print("[+] Requesting server get "+fileName)
        s.sendall(fileName.encode('utf-8'))
        receive_file(s, "client")
    else:
        print("[-] File Not on Server")
elif(REQUEST_TYPE == "put"):
    fileName = str(sys.argv[4])
    if(fileName in FILES_ON_SERVER):
        print("[-] File already exists on Server.")
    elif(fileName not in FILES_ON_CLIENT):
        print("[-] File not in client directory.")
    else:
        s.sendall("get".encode('utf-8'))
        print("[+] Requesting server to accept file.")
        send_file(s, fileName, "client")
elif(REQUEST_TYPE == "list"):
    print("[+] Files of Server")
    for files in FILES_ON_SERVER:
        print("   [+] "+files)

else:
    print("[!] Invalid Request")
s.close()
print("[-] Disconnected")
sys.exit(0)
