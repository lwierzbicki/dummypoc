#!/usr/bin/python3
#client.py

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#host = socket.gethostname()
host = "127.0.0.1"
port = 6666

client.connect((host, port)) # Connect to our client
msg = client.recv(1024)
client.close()

print (msg.decode('ascii'))