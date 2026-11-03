import socket

# 1. Inisialisasi socket TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 12345

# 2. Bind socket ke alamat dan port
server_socket.bind((HOST, PORT))
server_socket.listen(1) # Menunggu 1 koneksi masuk
print(f"[TCP SERVER] Berjalan di {HOST}:{PORT}. Menunggu koneksi client...")

# 3. Menerima koneksi dari client
client_socket, client_address = server_socket.accept()
print(f"[TCP SERVER] Terhubung dengan client dari: {client_address}")

try:
    while True:
        # 4. Menerima pesan dari client (maksimal 1024 bytes)
        data = client_socket.recv(1024).decode('utf-8')
        if not data or data.lower() == 'exit':
            print("[TCP SERVER] Client memutuskan koneksi.")
            break
        print(f"[Client]: {data}")

        # 5. Mengirim respon balik ke client
        response = f"Pesan '{data}' diterima dengan aman (TCP)."
        client_socket.send(response.encode('utf-8'))
finally:
    client_socket.close()
    server_socket.close()
    print("[TCP SERVER] Server dimatikan.")