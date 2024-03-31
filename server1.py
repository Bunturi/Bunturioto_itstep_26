import socket

# Server configuration
HOST = '127.0.0.1'
PORT = 65432

# Create a socket + Bind + Start listening
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
print(f"Waiting for connections on {HOST}:{PORT}")