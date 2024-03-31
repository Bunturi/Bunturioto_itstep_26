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
nicknames = []


# Broadcasts a message to all connected clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Handles communication with a single client.
def handle_client(client):
    while True:
        try:
            # Receive message from client
            message = client.recv(1024).decode()
            if message:
                index = clients.index(client)
                nickname = nicknames[index]
                # Append message to the chat log file
                with open("chat_log.txt", "a") as file:
                    file.write(f"{nickname} --> {message}\n")
                # Broadcast the message to all clients
                broadcast(message.encode())
        except Exception as e:
            print("Error:", e)
            # Handle client disconnection
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            broadcast(f"{nickname} left the chat".encode())
            break