import socket

host = "127.0.0.1"
port = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Menghubungkan ke server...")

client_socket.connect((host, port))

pesan = "Halo, ini simulasi OSI Layer"

client_socket.send(pesan.encode())

print("Data berhasil dikirim:")
print(pesan)

client_socket.close()

print("Client selesai.")