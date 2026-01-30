import socket
import threading
import sys

# Konfigurasi server
HOST = 'localhost'   # atau IP server
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("=== Terhubung ke Chat Room ===")

def receive_messages():
    """Thread untuk menerima pesan dari server"""
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if not message:
                print("\n[!] Koneksi ke server terputus.")
                break
            print(f"\n{message}")
        except:
            break

def send_messages():
    """Thread untuk mengirim pesan ke server"""
    while True:
        try:
            message = input()
            if message.lower() == 'exit':
                print("[!] Keluar dari chat.")
                client.close()
                sys.exit()
            client.send(message.encode('utf-8'))
        except:
            break

# Jalankan thread penerima
receive_thread = threading.Thread(target=receive_messages)
receive_thread.daemon = True
receive_thread.start()

# Jalankan thread pengirim
send_thread = threading.Thread(target=send_messages)
send_thread.start()