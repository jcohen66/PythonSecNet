from scapy.all import *

packets = rdpcap('packets.pcap')
packets.summary()
packets.sessions()
packets.show()

for packet in packets:
    packet.show()
    print(packet.summary())

def get_packet_layer(packet):
    yield packet.name
    while packet.payload:
        packet = packet.payload
        yield packet.name

for packet in packets:
    layers = list(get_packet_layer(packet))
    print("/".join(layers))
    