#!/usr/bin/python3
# simple socket connection

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#host = socket.gethostname()
host = "127.0.0.1"
port = 6666

try:
    client.connect((host, port)) # Connect to our client
    msg = client.recv(1024)
    client.close()
except ConnectionRefusedError:
    print ("The server is not accepting our connection request!")
    exit(1)

print (msg.decode('ascii'))