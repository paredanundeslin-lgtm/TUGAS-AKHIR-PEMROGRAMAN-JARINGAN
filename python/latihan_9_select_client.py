import socket
import select
import sys

def run_chat_client():
    server_ip = '127.0.0.1'
    server_port = 9000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    client_socket.setblocking(False)

    print("=== Terhubung ke Chat Server (Select) ===")
    print("Ketik pesan dan tekan Enter")
    print("Ctrl+C untuk keluar\n")

    while True:
        # Satpam client: pantau STDIN & socket server
        read_list = [sys.stdin, client_socket]

        read_sockets, _, _ = select.select(read_list, [], [])

        for sock in read_sockets:
            # KASUS 1: User mengetik
            if sock == sys.stdin:
                message = sys.stdin.readline()
                if message:
                    client_socket.send(message.encode())

            # KASUS 2: Server mengirim pesan
            else:
                data = sock.recv(1024)
                if not data:
                    print("\n[!] Server menutup koneksi.")
                    return
                else:
                    print(data.decode(), end="")

if __name__ == "__main__":
    run_chat_client()