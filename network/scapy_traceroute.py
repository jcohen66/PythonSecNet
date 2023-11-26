"""
IP packets include an attribute (TTL) where you indicate the lifetime of the
packet. This way, every time a device receives an IP packet, it decreases the TTL (package lifetime)
by 1 and passes it to the next machine. Basically, it is a smart way to make sure that packets do
not loop infinitely. When the TTL reaches 0, the packet is discarded and an ICMP message is sent.
"""

from scapy.all import *
host = "45.33.32.156"
for i in range(1, 20):
    packet = IP(dst=host, ttl=i) / UDP(dport=40000)
    # Send the packet and get a reply
    reply = sr1(packet, timeout=2, verbose=0)
    if reply is None:
        print(str(i) + " " + "Timeout")
    elif reply.type == 3:
        print(str(i) + " " + f"Done! {reply.src}")
        break
    elif reply.type == 11:
        print(str(i) + " " + "Time exceeded")
    elif reply.type == 0:
        print(str(i) + " " + "Echo reply")
        break
    else:
        print(f"{i} hops away: {reply.src}")
