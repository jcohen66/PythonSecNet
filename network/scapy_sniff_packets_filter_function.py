from scapy.all import *

"""
Check whether the sniffed packet
has an IP layer; if it has an IP layer, then we store the source, destination, and TTL values of the
sniffed packet and print them out.
"""

def sniffPackets(packet):
    if packet.haslayer(IP):
        ip_layer = packet.getlayer(IP)
    packet_src = ip_layer.src
    packet_dst = ip_layer.dst
    print("[+] New Packet: {src} -> {dst}".format(src=packet_src,
                                                  dst=packet_dst))


if __name__ == '__main__':
    interfaces = get_if_list()
    print(interfaces)
    for interface in interfaces:
        print(interface)
        interface = input("Enter interface name to sniff: ")
        print("Sniffing interface " + interface)
        sniff(iface=interface, filter="tcp and (port 443 or port 80)",prn=sniffPackets)
