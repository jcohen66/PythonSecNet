import socket

"""
If you try to get information about specific domains or
IP addresses that don’t exist, it will probably throw a socket.gaierror exception, showing the
message [Errno -2] Name or service not known.

If the connection with our target is not possible, it will throw a socket.error exception with the message Connection error: [Errno 10061] No connection.
This message means the target machine actively refused its connection and communication cannot be established in the specified port, the port has been closed, or
the target is disconnected.
"""

host = "domain/ip_address"
port = 80

# Create a socket object
try:
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"Socket created successfully: {mysocket}")
    mysocket.settimeout(5)
except socket.error as error:
    print(f"Socket creation failed with error {error}")

# Connect the socket to a server
try:
    mysocket.connect((host, port))
    print(mysocket)
    print(f"Timeout error: {error}")
except socket.gaierror as error:
    print(f"Socket connection error to server error {error}")
except socket.error as error:
    print(f"Socket connection failed with error {error}")