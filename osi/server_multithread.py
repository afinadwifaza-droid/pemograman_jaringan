import socket
import threading

def handle_client(client_socket, client_address):
    """Fungsi ini berjalan di thread terpisah untuk setiap client."""
    print(f"[+] Jalur baru dibuka untuk client: {client_address}")
    try:
        # Menerima data dari client
        data_diterima = client_socket.recv(1024).decode('utf-8')
        print(f"[{client_address}] Mengirim: {data_diterima}")

        # Kirim balik respon
        respon = f"Halo! Pesanmu '{data_diterima}' diproses di thread: {threading.current_thread().name}"
        client_socket.send(respon.encode('utf-8'))
    except Exception as e:
        print(f"[!] Error saat melayani {client_address}: {e}")
    finally:
        # Pastikan koneksi ditutup setelah selesai
        client_socket.close()
        print(f"[-] Koneksi dengan {client_address} selesai. Jalur ditutup.")

def start_server():
    SERVER_IP = "127.0.0.1"
    SERVER_PORT = 5005

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen(5) # Mengizinkan antrean hingga 5 client
    print(f"[*] Multi-threaded Server berjalan di {SERVER_IP}:{SERVER_PORT}...")

    try:
        while True:
            # Menerima koneksi baru
            client_socket, client_address = server_socket.accept()

            # Membuat thread baru khusus untuk client yang baru masuk
            client_thread = threading.Thread(
                target=handle_client,
                args=(client_socket, client_address)
            )
            # Memulai thread (berjalan asinkron di latar belakang)
            client_thread.start()
            print(f"[*] Total thread aktif: {threading.active_count() - 1}")

    except KeyboardInterrupt:
        print("\n[*] Server dimatikan oleh admin.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()