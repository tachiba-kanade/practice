"""Nodes either c2c , or server to client - P2P

so usually servers listen to the client so they are waiting for the client to send a request and server sends a response.
so generally 2 things are important 
1. Port numbers
2. Type of Connections we will build - 
TCP(transmission control protocol)- connection orriented network meaning i have to establish/create a connection 
and then you can communicate. 
UDP(connectionless network) - User Datagram protocol, just the package is send without any confirmity

so we have public IP addresses and private IP Address, so if a machine with multiple services so each service will have a port number

"""


from http import client
import socket

# we have to pass 2 things here first one is the type of network im working with ipV4, ipv6 and second its TCP or UDP here its ipv4 and TCP
s = socket.socket() # default 4 and tcp

print("Server socket created")

# bind socket with port number

s.bind(('localhost',9999))# pass port number ,mostly will be different one client of server 0 - 65535

# now we have to start listening to the client and then connect to clients and at once how many clients you wanna connect
# create a queue for 5 connections or 10 connections or 3 so mean 3 clients will wait for response/cnnection

s.listen(3)
print("Waiting for Connections")

while True:
    c, addr = s.accept() #accept the connection from the client - socket and address
    print("Connected with", addr)
    c.send(bytes("Welcome. to Telusko","utf-8")) # this cant be send in string format it has to be byte format
    c.close()

#A protocol like HTTP uses a socket for only one transfer. The client sends a request, then reads a reply. 
# That’s it. The socket is discarded. This means that a client can detect the end of the reply by receiving 0 bytes.