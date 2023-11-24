import socket
import sys
from datetime import datetime
import errno

remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)
print("Please enter the range of ports to scan")
startPort = int(input("Enter the start port number: "))
endPort = int(input("Enter the end port number: "))
print("Please wait, scanning remote host", remoteServerIP)
time_init = datetime.now()
try:
    for port in range(startPort, endPort):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((remoteServerIP, port))
        print(f"Port {port}: ", 'CLOSED' if result > 0 else 'OPEN' )
        sock.close()
except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved. Exiting")
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

time_end = datetime.now()
total_time = time_end - time_init
print(f"Scanning Completed in: {total_time}")