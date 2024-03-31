import socket

# Server configuration
HOST = '127.0.0.1'
PORT = 65432

# Create a socket + Bind + Start listening
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
print(f"Waiting for connections on {HOST}:{PORT}")

while True:
    # Accept incoming connection
    conn, addr = server_socket.accept()

    print('Connected by', addr)
    message = "server accepted Connection"
    conn.sendall(message.encode())
    conn.close()