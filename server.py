import socket
#this is server.py
s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host,port))

s.listen(5)
while True:
	c, addr = s.accept()
	print("Got Connection from", addr)
	c.send("Thanks for connecting")
	c.close()
