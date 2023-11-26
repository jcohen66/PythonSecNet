from scapy.all import *
"""
Extract the client and server identifiers.
"""
pcap_path = "packets_DHCP.pcap"
packets = rdpcap(pcap_path)
for packet in packets:
    try:
        packet.show()
        options = packet[DHCP].options
        for option in options:
            if option[0] == "client_id":
                client_id = option[1].decode("utf-8")
            if option[0] == "server_id":
                server_id = option[1]
                print(f"ServerID: {server_id}  ClientID: {client_id}")
    except IndexError as error:
        print(error)

