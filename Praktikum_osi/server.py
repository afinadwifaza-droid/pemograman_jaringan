import socket

host = "127.0.0.1"
port = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print("Server berjalan...")
print(f"Menunggu koneksi di {host}:{port}")

conn, addr = server_socket.accept()

print(f"Client terhubung dari {addr}")

data = conn.recv(1024)

print("Data diterima:")
print(data.decode())

conn.close()
server_socket.close()

print("Server selesai.")