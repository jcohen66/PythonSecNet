from scapy.all import *
import sys

# Create a packet with ICMP layer
packet=IP(dst='www.python.org')/ICMP()
packet.show()

# Send the packet but not get the response
sendp(packet)

