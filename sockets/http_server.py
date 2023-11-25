import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind(("localhost", 8080))
my_socket.listen(5)

# Keep the connection alive
while True:
    print("Waiting for connections...")
    (recv_socket, address) = my_socket.accept()
    print("HTTP request received:")
    print(recv_socket.recv(1024))
    recv_socket.send(bytes("HTTP/1.1 200 OK\r\n\r\n <html><body><h1>Hello World!</h1></body></html> \r\n", "utf-8"))
    recv_socket.close()

