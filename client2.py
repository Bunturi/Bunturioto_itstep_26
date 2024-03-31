import socket

# Server configuration
SERVER_IP = "127.0.0.1"
SERVER_PORT = 45678

# Prompt the user to enter a nickname
nickname = input("Enter your nickname: ")

# Create a socket object for the client + Connect
client_socket = socket.socket()
client_socket.connect((SERVER_IP, SERVER_PORT))


# Receives messages from the server
def receive():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message == "Nickname":
                client_socket.send(nickname.encode())
            else:
                print(message)
        except Exception as e:
            print("Error", e)
            client_socket.close()
            break