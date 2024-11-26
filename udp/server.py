import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('127.0.0.1', 8080))

print("UDP server is up and listening on port 8080...")

while True:
    data, client_address = server_socket.recvfrom(1024)
    print(f"Received message from client: {data.decode()}")

    server_socket.sendto(data, client_address)
    print(f"Echoed back to {client_address}")
