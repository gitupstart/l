import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8080))
server_socket.listen(1)

print("Server is listening on port 8080...")
conn, addr = server_socket.accept()
print(f"Connected to client at {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break
    print(f"Received: {data.decode()}")
    conn.sendall(data)

conn.close()
server_socket.close()
