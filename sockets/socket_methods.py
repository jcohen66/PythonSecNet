import socket

try:
    hostname = socket.gethostname()
    print("gethostname:", hostname)
    ip_address = socket.gethostbyname(hostname)
    print("Local IP Address:", ip_address)
    print("gethostbyname:", socket.gethostbyname('www.python.org'))
    print("gethostbyname_ex:", socket.gethostbyname_ex('www.python.org'))
    print("gethostbyaddr:", socket.gethostbyaddr('8.8.8.8'))
    print("getfqdn:", socket.getfqdn('www.google.com'))
    print("gethostbyname_ex:", socket.gethostbyname_ex('www.google.com'),None,0,socket.SOCK_STREAM)

except Exception as error:
    print(str(error))
    print("Connection error")