import socket
import sys
import time

s=socket.socket()
host =socket.gethostname()
print("Server Will start on host : ", host)
port=8080
s.bind((host,port))
print("")
print("Server done binding to host and port Sucessfully")
print("")
print("Server is waiting for incoming Connection ")
s.listen(1)
conn, addr=s.accept()
print(addr,"Has connected to server and is now online ...")
print("")
while 1:
            message=input(str(">> "))
            message=message.encode()
            conn.send(message)
            print("Message has been sent...")
            print("")
            incoming_message = conn.recv(1024)
            incoming_message = incoming_message.decode()
            print("Client : ", incoming_message)
            print("")


