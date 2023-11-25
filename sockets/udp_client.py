import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 6789

address = (SERVER_IP, SERVER_PORT)
socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Enter your message: ")
    socket_client.sendto(message.encode("utf-8"), address)
    if message == "quit":
        break
    else:
        data, address = socket_client.recvfrom(4096)
        print(f"[*] Message received from server: {data.decode()}")

socket_client.close()