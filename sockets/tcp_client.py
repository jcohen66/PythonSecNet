import socket

host = "127.0.0.1"
port = 9999

try:
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.settimeout(10)
    my_socket.connect((host, port))
    print(f"[*] Connection established to {host} on port {port}")
    message = my_socket.recv(1024)
    print(f"[*] Message received from server: {message}")

    # Keep the connection alive
    while True:
        message = input("Enter your message: ")
        # Encode the data to bytes and send it to the client
        my_socket.send(message.encode("utf-8"))
        if message == "quit":
            break
        else:
            message = my_socket.recv(1024)
            # When its byte data, we need to decode it
            print(f"[*] Message received from server: {message.decode()}")

except socket.errno as error:
    print(f"Socket connection error: {error}")
finally:
    my_socket.close()