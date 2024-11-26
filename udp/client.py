import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 8080)
message = "Hello, UDP Server!"

client_socket.sendto(message.encode(), server_address)
print(f"Sent message to server: {message}")

data, _ = client_socket.recvfrom(1024)
print(f"Received from server: {data.decode()}")

client_socket.close()
