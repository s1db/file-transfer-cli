import socket
import os
import sys

def send_file(s, fileName, sendFrom):
    # get file name to send
    try:
        filePath = r"./"+sendFrom+"/"+fileName
        s.sendall(str(os.path.getsize(filePath)).encode('utf-8'))
        s.sendall(fileName.encode('utf-8'))
        # open file
        with open(filePath, "rb") as f:
            # send file
            print("[+] Attempting to send file: "+fileName)
            data = f.read()
            s.sendall(data)
            print("[+] Successfully Sent: " + fileName)
    except Exception as e:
        print("[!] Unable to send file. Refer to the following error:")
        print(e)
        exit(1)

def receive_file(s, receiveTo):
    try:
        fileLength = int(s.recv(512).decode())
        fileName = s.recv(1024).decode()
        filePath = r"./"+receiveTo+"/"+fileName
        print("[+] Attempting to download file: " + fileName)
        f = open(filePath, "wb")
        while fileLength>0:
            data = s.recv(4096)
            if not data:
                if fileLength >0:
                    print("[!] Unsuccessful Download.")
                    f.close()
                    os.remove(filePath)
                break
            f.write(data)
            fileLength-=4096
        f.close()    
        print("[+] Successfully Received: " + fileName)
    except Exception as e:
        try:
            f.close()
            os.remove(filePath)
        except:
            pass
        print("[!] Unable to receive file. Refer to the following error:")
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