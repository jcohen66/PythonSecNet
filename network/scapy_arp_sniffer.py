import scapy.all as scapy

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def get_mac_address(ip_address):
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request = scapy.ARP(pdst=ip_address)
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][0][1].hwsrc

def process_sniffed_packet(packet):
    """
    Check whether the sniffed packet has an ARP layer and whether the ARP layer is an ARP response
    :param packet:
    :return:
    """
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
        try:
            real_mac = get_mac_address(packet[scapy.ARP].psrc)
            response_mac = packet[scapy.ARP].hwsrc
            if real_mac != response_mac:
                print("[+] ALERT!!! You are under attack!!! ARP Table is being poisoned!!!")
        except IndexError:
            pass

if __name__ == '__main__':
    sniff("en0")