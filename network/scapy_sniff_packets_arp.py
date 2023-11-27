from scapy.all import *

"""
Analyze the ARP packets that are exchanged on an interface. The Address Resolution Protocol (ARP) is a protocol that communicates with hardware interfaces at the data
link layer and provides services to the upper layer.
"""

def arpDisplay(packet):
    if packet.haslayer(ARP):
        # Request
        if packet[ARP].op ==1:
            return "Request: {} is asking about {}".format(packet[ARP].psrc, packet[ARP].pdst)
        # Response
        if packet[ARP].op ==2:
            return "*Response: {} has address {}".format(packet[ARP].hwsrc, packet[ARP].psrc)

def main():
    sniff(iface="en0", filter="arp", prn=arpDisplay,store=0, count=10)

if __name__ == "__main__":
    main()