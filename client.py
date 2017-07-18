import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host,port))

def sending(message):
    print s.send(message)

def receiving(message):
    print s.recv(message)

receiving(1024)
s.close()
