import socket

bind_ip = '0.0.0.0'
bind_port = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)  # max backlog of connections

print('Listening on {}:{}'.format(bind_ip, bind_port))

client_sock, address = server.accept()
while True:
    print('Accepted connection from {}:{}'.format(address[0], address[1]))
    data = client_sock.recv(1024)
    if int(data) == 1:
        print("GOt 1")
    if int(data) == 2:
        print("GOt 2")
    if int(data) == 3:
        print("GOt 3")
    if int(data) == 4:
        print("GOt 4")
    print(data)

