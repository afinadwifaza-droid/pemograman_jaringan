import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, SERVER_PORT))
print("[TCP CLIENT] Berhasil terhubung ke server!")

pesan = input("Ketik pesan: ")
client.send(pesan.encode("utf-8"))

balasan = client.recv(1024).decode("utf-8")
print(f"[Balasan Server] {balasan}")

client.close()