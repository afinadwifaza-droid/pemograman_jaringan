import socket

# 1. Inisialisasi socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 12345

# 2. Melakukan koneksi ke server (Handshake)
print("[TCP CLIENT] Menghubungkan ke server...")
client_socket.connect((HOST, PORT))
print("[TCP CLIENT] Berhasil terhubung!")

print("Ketik pesan Anda (Ketik 'exit' untuk keluar):")
try:
    while True:
        message = input("> ")
        # 3. Mengirim pesan ke server
        client_socket.send(message.encode('utf-8'))

        if message.lower() == 'exit':
            break

        # 4. Menerima respon balik dari server
        response = client_socket.recv(1024).decode('utf-8')
        print(f"[Server]: {response}")
finally:
    client_socket.close()
    print("[TCP CLIENT] Koneksi ditutup.")