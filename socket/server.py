import socket

host = 'localhost'
port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)

print('waiting for a connection')
connection, client = sock.accept()
print(client, 'connected')

data = connection.recv(16)
print('received "%s"' % data.decode())
if data:
    connection.sendall(data)
else:
    print('no data from', client)

connection.close()
sock.close()