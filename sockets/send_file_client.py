import os
import socket
import struct

def send_file(sock: socket.socket, filename):
    # Get the size of the file
    filesize = os.path.getsize(filename)

    # Pack the size of the file into a binary format
    sock.sendall(struct.pack("<Q", filesize))

    # Open the file and send it
    with open(filename, "rb") as file:
        #
        while read_bytes := file.read(4096):
            sock.sendall(read_bytes)

with socket.create_connection(("localhost", 9999)) as connection:
    print("[*] Connecting to server...")
    print("[*] Sending file...")
    # Send the file
    send_file(connection, "send_file_client.py")
    print("[*] File sent successfully")