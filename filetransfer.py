import socket
import os
import sys
def receive_file(s, receiveTo):
    fileName = s.recv(1024).decode()
    filePath = r"./"+receiveTo+"/"+fileName
    print("path where will be save: "+filePath)
    f = open(filePath, "wb")
    while True:
        # get file bytes
        data = s.recv(4096)
        if not data:
            break
        # write bytes on file
        f.write(data)
    f.close()
    print("[+] Download complete!")
    print("received: "+ fileName)


def send_file(s, fileName, sendFrom):
    # get file name to send
    s.sendall(fileName.encode('utf-8'))
    filePath = r"./"+sendFrom+"/"+fileName
    # open file
    with open(filePath, "rb") as f:
        # send file
        print("[+] Sending file...")
        data = f.read()
        s.sendall(data)
        print("sent: "+ fileName)


def list_dir():
    files_array = os.listdir("./server/")
    for file in files_array: 
        print(file)