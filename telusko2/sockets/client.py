import socket

c = socket.socket()

c.connect(("localhost",9999)) # ip adress and port number

print (c.recv(1024).decode())