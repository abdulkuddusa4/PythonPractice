import socket
from shortcuts import *




server = socket.socket()
try:
    server.bind(('localhost',3000))
    print("running at port 3000")
except OSError:
    server.bind(('localhost',4000))
    print("running at port 4000")

server.listen()
print("server started")

while True:

    client,addr = server.accept()
    client.send(get_response('templates/index.html'))
    client.close()

