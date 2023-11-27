from scapy.all import *

def count_dns_request(packet):
    # Could also use 'if DNSRR in packet' to check for DNS response
    if packet.haslayer(DNSRR) and packet.getlayer(UDP).sport == 53:
        print(packet.summary())
        print(packet.show())


if __name__ == '__main__':
    sniff(iface='en0', filter="udp and port 53", prn=count_dns_request, count=100)