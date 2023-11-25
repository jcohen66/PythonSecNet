import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_IP, SERVER_PORT))
server.listen(5)
print(f"[*] Server listening on {SERVER_IP}:{SERVER_PORT}")
client, address = server.accept()

client.send(b"I am the server accepting connections on port 9999")
print(f"[*] Accepted connection from {address[0]}:{address[1]}")

# Keep the connection alive
while True:
    # When its byte data, we need to decode it
    request = client.recv(1024).decode()
    print(f"[*] Received: {request}")
    if request != "quit":
        # Encode the data to bytes and send it to the client
        client.send(bytes("ACK!", "utf-8"))
    else:
        break

client.close()
server.close()


