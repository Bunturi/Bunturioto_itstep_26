import socket
import threading

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


def recived():
    while True:
        client, address = server_socket.accept()
        print(f"Connection established with {address}")

        # Send a prompt for the client to provide a nickname
        client.send("Nickname".encode())
        nickname = client.recv(1024).decode()
        # Add the client and its nickname to the lists
        nicknames.append(nickname)
        clients.append(client)

        print(f"{nickname} connected")
        # Broadcast a message indicating the client has joined the chat
        broadcast(f"{nickname} joined the chat".encode())

        # Start a new thread to handle communication with the client
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

recived()

