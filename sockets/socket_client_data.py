import socket
host = input("Enter the host name to connect: ")
port = int(input("Enter the port number to connect: "))

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
        socket_tcp.settimeout(10)
        if (socket_tcp.connect_ex((host, port)) == 0):
            print(f"Establisted connection to {host} on Port {port}")
            request = 'GET / HTTP/1.1\r\nHost: " + host + "\r\n\r\n"'
            socket_tcp.send(request.encode())
            data = socket_tcp.recv(4096)
            print("Data:", repr(data))
            print("Length of data:", len(data))
except socket.timeout as error:
    print(f"Socket connection timeout error: {error}")
except socket.gaierror as error:
    print(f"Socket connection error to server: {error}")
except socket.error as error:
    print(f"Socket connection error: {error}")
