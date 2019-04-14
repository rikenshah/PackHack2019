import socket, json, time
import pprint as pp
from coordinates import Coordinate
import threading

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = "0.tcp.ngrok.io"
port = 19411

###
bind_ip = "0.0.0.0"
bind_port = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)  # max backlog of connections
print('Listening on {}:{}'.format(bind_ip, bind_port))

def handle_client_connection(client_socket):
    request = client_socket.recv(1024)
    print('Received {}'.format(request))
    client_socket.send('ACK!')
    client_socket.close()
###

s.connect((host,port))

a = '''
{
    "category": "tracker",
    "request" : "get",
    "values": [ "push", "iscalibrated" ]
}
'''

s.sendall(a.encode())
print(s.recv(port))

print("++++++++++++++++++++")

b = '''
{
    "category": "tracker",
    "request" : "get",
    "values": [ "frame" ]
}
'''


s.sendall(b.encode())
print(s.recv(port))

