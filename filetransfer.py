import socket
import os
import sys
'''
TODO:
[] Write a receive all function to check if all packets have been received.
[] Sending the directory, send individually.
'''

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

#def receive_all(s)

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
        filesListString = ""
        for file in filesList:
            filesListString += str(file)+"?"
        s.sendall(filesListString.encode('utf-8')) #? can't be in a file name therefore we use it as a magic string.
    except Exception as e:
        print(e)
        exit(1)


def receive_listing(s, receivedTo):
    try:
        fileList = str(s.recv(1024).decode()).split("?")
        return fileList[0:-1]
    except Exception as e:
        print(e)
        exit(1)