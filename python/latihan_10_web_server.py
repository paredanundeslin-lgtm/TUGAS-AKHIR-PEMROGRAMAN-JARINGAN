import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8080))
server.listen(1)

print("=== Web Server berjalan di http://localhost:8080 ===")

while True:
    conn, addr = server.accept()
    print(f"Koneksi dari {addr}")

    # Terima request browser
    request = conn.recv(1024).decode()
    print("----- HTTP REQUEST -----")
    print(request)

    # HTTP Response (WAJIB FORMAT BENAR)
    response = """HTTP/1.1 200 OK
Content-Type: text/html

<html>
  <body>
    <h1>Halo Semua!</h1>
    <p>Ini web server buatan sendiri</p>
  </body>
</html>
"""

    conn.send(response.encode())
    conn.close()