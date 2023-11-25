import socket
import struct

def receive_file_size(sock: socket.socket) -> int:
    fmt = "<Q"
    expected_size = struct.calcsize(fmt)
    received_bytes = 0
    stream = bytes()

    # Keep receiving chunks until we get the expected size
    while received_bytes < expected_size:
        chunk = sock.recv(expected_size - received_bytes)
        stream += chunk
        received_bytes += len(stream)

    # Unpack the size of the file from the stream
    filesize = struct.unpack(fmt, stream)[0]
    return filesize

def receive_file(sock: socket.socket, filename: str):
    # Get the size of the file
    filesize = receive_file_size(sock)

    # Open the file and receive the data
    with open(filename, "wb") as file:
        received_bytes = 0
        while received_bytes < filesize:
            chunk = sock.recv(1024)
            if chunk:
                file.write(chunk)
                received_bytes += len(chunk)

with socket.create_server(("localhost", 9999)) as server:
    print("[*] Waiting for connections...")
    (connection, address) = server.accept()
    print(f"[*] Connection to {address[0]}:{address[1]} established")
    print("[*] Receiving file...")
    receive_file(connection, "_file_received.py")
    print("[*] File received successfully")