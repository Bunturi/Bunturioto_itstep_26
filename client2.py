import socket

# Server configuration
SERVER_IP = "127.0.0.1"
SERVER_PORT = 45678

# Prompt the user to enter a nickname
nickname = input("Enter your nickname: ")

# Create a socket object for the client + Connect
client_socket = socket.socket()
client_socket.connect((SERVER_IP, SERVER_PORT))