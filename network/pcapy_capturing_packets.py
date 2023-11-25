import pcapy
import datetime
interfaces = pcapy.findalldevs()
print(f"Available Interfaces: {interfaces}")
for interface in interfaces:
    print(f"Interface: {interface}")
interface = input("Enter the interface name: ")
print(f"Sniffing on {interface}")
cap = pcapy.open_live(interface, 65536, True, 0)
while True:
    (header, payload) = cap.next()
    print(f"Captured {len(payload)} bytes {datetime.datetime.now()} {header.getlen()}" )
