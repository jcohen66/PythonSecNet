import sys
from scapy.all import *

target = sys.argv[1]
icmp = IP(dst=target)/ICMP()
recv = sr1(icmp, timeout=10)
if recv:
    print("Target is up")