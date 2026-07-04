import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    ip = socket.gethostbyname("www.google.com")
    print("CONNECT SUCCESSFULL", ip)
except socket.gaierror:
    #A socket.gaierror is a Python network exception raised when the operating system's getaddrinfo() 
    # function fails to translate a hostname (e.g., ://example.com) into an IP address. 
    # It stands for GetAddressInfo Error
    print ("there was an error resolving the host")
    sys.exit() 





"""
For a server client program

server
First of all, we import socket which is necessary. 
Then we made a socket object and reserved a port on our pc.
After that, we bound our server to the specified port. Passing an empty string means that the server can listen to incoming connections from other computers as well. If we would have passed 127.0.0.1 then it would have listened to only those calls made within the local computer.
After that we put the server into listening mode.5 here means that 5 connections are kept waiting if the server is busy and if a 6th socket tries to connect then the connection is refused.
At last, we make a while loop and start to accept all incoming connections and close those connections after a thank you message to all connected sockets.
"""

s = socket.socket()
port = 9000
s.bind(port)
s.listen(5)

while True:
    c, addr = s.accept()
    s.send(bytes("thank you","utf-8"))
    