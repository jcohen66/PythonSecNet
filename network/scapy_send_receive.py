from scapy.all import *

#
packet=Ether()/IP(dst='www.python.org')/TCP(dport=80,flags='S')
packet.show()

# Send the packet and get the response
srp1(packet, timeout=10)



