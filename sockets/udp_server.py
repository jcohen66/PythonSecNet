"""
The main difference between TCP
and UDP is that UDP is not connection-oriented, and this means that there is no guarantee our
packets will reach their destinations, and no error notification if a delivery fails.
"""

import socket, sys

SERVER_IP = '127.0.0.1'
SERVER_PORT = 6789

socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_server.bind((SERVER_IP, SERVER_PORT))
print(f"[*] Server listening to {SERVER_IP}:{SERVER_PORT}")

while True:
    data, address = socket_server.recvfrom(4096)
    socket_server.sendto(f"[*] Server UDP Listening on {SERVER_IP}:{SERVER_PORT}".encode(), address)
    data.strip()
    if data == b"quit":
        break

    # When its byte data, we need to decode it
    print(f"[*] Message received {data.decode()} from {address[0]}:{address[1]}")
    try:
        response = f"Hi {sys.platform}"
    except Exception as error:
        response = sys.exc_info()[0]
    print("Response:", response)
    # Encode the data to bytes and send it to the client
    socket_server.sendto(response.encode("utf-8"), address)

socket_server.close()