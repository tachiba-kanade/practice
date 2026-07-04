import socket

c = socket.socket()

c.connect(("localhost",5000)) # ip adress and port number

while True:
    s, addr = c.accept()
    print (c.recv(1024).decode())
    s.send(bytes ("Hello there", "utf-8"))


