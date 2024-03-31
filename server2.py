import socket

# Server configuration
HOST = '127.0.0.1'
PORT = 65432

# Create a socket and start listening
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")

server_socket.bind((HOST, PORT))
server_socket.listen()
print(f"Start listening on {PORT}")

clients = []


# Broadcasts a message to all connected clients
def broadcast(message):
    for client in clients:
        client.send(message)
