import socket
import os
import sys


def receive_file(s, receiveTo):
    fileName = s.recv(1024).decode()
    filePath = r"./"+receiveTo+"/"+fileName
    try:
        print("[+] Attempting to download file: " + fileName)
        f = open(filePath, "wb")
        while True:
            data = s.recv(4096)
            if not data:
                break
            f.write(data)
        f.close()    
        print("[+] Successfully Received: " + fileName)
    except Exception as e:
        print(e)
        exit(1)

def send_file(s, fileName, sendFrom):
    # get file name to send
    try:
        s.sendall(fileName.encode('utf-8'))
        filePath = r"./"+sendFrom+"/"+fileName
        # open file
        with open(filePath, "rb") as f:
            # send file
            print("[+] Attempting to send file: "+fileName)
            data = f.read()
            s.sendall(data)
            print("[+] Successfully Sent: " + fileName)
    except Exception as e:
        print(e)
        exit(1)

def send_listing(s, sendFrom):
    try:
        filesList = os.listdir(r"./"+sendFrom)
        s.sendall(str(filesList).encode('utf-8'))
    except Exception as e:
        print(e)
        exit(1)
def receive_listing(s, receivedTo):
    try:
        fileList = str(s.recv(1024).decode()).replace('"', '').replace('\'', '').strip('][').split(', ')
        return fileList
    except Exception as e:
        print(e)
        exit(1)