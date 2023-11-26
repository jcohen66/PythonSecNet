from scapy.all import *

"""
Usage:

sudo python3 network/scapy_tcp_target.py 45.33.32.156 80
"""

# we can target the IP and metadata since we received a response
# confirmation packet. We can also target the port.
target = sys.argv[1]
port = int(sys.argv[2])
ans, unans = sr(IP(dst=target)/TCP(dport=port, flags="S"))
ans.summary()