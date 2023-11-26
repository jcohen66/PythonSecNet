import pcapy
import datetime

interfaces = pcapy.findalldevs()
print("Available interfaces are :")
for interface in interfaces:
    print(interface)
interface = input("Enter interface name to sniff : ")
if interface != 'any' and interface not in interfaces:
    print(f"\nInterface {interface} not found")
    exit(1)
print("Sniffing interface " + interface)
cap = pcapy.open_live(interface, 65536, 0, 0)
while True:
    (header, payload) = cap.next()
    print('%s: captured %d bytes' % (datetime.datetime.now(), header.getlen()))
