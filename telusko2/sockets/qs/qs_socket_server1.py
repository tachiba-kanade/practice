"""
Level 1 — Basic Client-Server Echo
Project: Echo Server

Build a server that accepts one client connection and sends back whatever the client sends.

You practice
Creating a socket
Binding host and port
Listening for connections
Accepting a client
Sending and receiving bytes
Encoding and decoding strings
Requirements

Server:

Server starts on localhost:5000
Client connects
Client sends: hello
Server responds: hello

Client:

Connects to server
Takes user input
Sends it
Prints server response
Brainstorm questions
What happens if the client sends an empty message?
What happens if the server is not running?
Why do we need .encode() and .decode()?
What does recv(1024) actually mean?
Can one server handle multiple messages from the same client?
Small challenge

Keep the connection alive until the client types:

exit

"""

import sys 
import socket

from idna import encode
import client

s = socket.socket()
port = 5000
# s.connect(port)
s.bind(port)
print("SOCKET CONNECTED TO THE CLIENT ", port)
s.listen(1)

while True:
    c, addr = s.accept()
    s.recv(1024).decode()
    s.send(bytes("Hello", "utf-8"))

