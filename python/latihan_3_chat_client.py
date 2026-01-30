import socket

# Persiapan Socket Client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Hubungkan ke server
client.connect(('localhost', 5000))
print("=== Terhubung ke Chat Server ===")

while True:
    try:
        # 1. Kirim pesan ke server
        message = input("Client (Anda) > ")
        client.send(message.encode('utf-8'))

        # Cek jika client ingin keluar
        if message.lower() == 'bye':
            print("[!] Anda mengakhiri sesi.")
            break

        # 2. Terima balasan dari server (BLOCKING)
        reply = client.recv(1024).decode('utf-8')

        if not reply or reply.lower() == 'bye':
            print("[!] Server mengakhiri sesi.")
            break

        print(f"Server > {reply}")

    except Exception as e:
        print(f"Error Terjadi: {e}")
        break

# Tutup koneksi
client.close()
print("=== Aplikasi Client Ditutup ===")