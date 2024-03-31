import socket

# Server configuration
HOST = '127.0.0.1'
PORT = 65432

# Create a socket + connection + Receive and print
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
received_message = client_socket.recv(1024).decode()
print(received_message)
client_socket.close()