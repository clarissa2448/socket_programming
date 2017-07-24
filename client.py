#this is client.py
import socket
import lifxlan
#ignore functions for now

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host,port))
print (s.recv(12))
s.send("123")
s.close()
