import sys
from scapy.all import *
import logging

"""
Usage:

sudo python3 network/scapy_port_scan.py scanme.nmap.org 20 23 1
sudo python3 network/scapy_port_scan.py scanme.nmap.org 20 23 0
"""

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


def analyze_port(host, port, verbose_level):
    print("[+] Analyzing port " + str(port))
    packet = IP(dst=host) / TCP(dport=port, flags="S")
    response = sr1(packet, timeout=0.5, verbose=verbose_level)
    if response is not None and response.haslayer(TCP):
        if response.getlayer(TCP).flags == 18:
            print("[+] Port " + str(port) + " is open")
        elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14:
            print("[+] Port " + str(port) + " is closed")
        elif response.haslayer(ICMP):
            if int(response.getlayer(ICMP).type) == 3 and int(response.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]:
                print("[+] Port " + str(port) + " is filtered")


if __name__ == '__main__':
    if len(sys.argv) < 5:
        print("usage: %s target startport endport verbose_level" % (sys.
        argv[0]))
        sys.exit(0)
    target = str(sys.argv[1])
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3]) + 1
    verbose_level = int(str(sys.argv[4]))
    print("Scanning " + target + " for open TCP ports\n")
    for port in range(start_port, end_port):
        analyze_port(target, port, verbose_level)
