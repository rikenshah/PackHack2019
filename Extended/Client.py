import socket, random, time

ip_address = '0.tcp.ngrok.io'
port = 11561

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip_address, port))


while True:
    z = str(random.randint(1,4))
    print(z)
    s.sendall(z.encode())
    time.sleep(1)

s.close()