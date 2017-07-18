#this is client.py
import socket
#ignore functions for now
def sending(message):
    print s.send(message)

def receiving(message):
    print s.recv(message)

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host,port))
print s.recv("hi")
s.close()
