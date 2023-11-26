from scapy.all import *

packetCount = 0


def customAction(packet):
    global packetCount
    packetCount += 1
    return "{} {} → {}".format(packetCount, packet[0][1].src, packet[0][1].dst)

# Apply the customAction function to each sniffed packet
sniff(filter="ip", prn=customAction)
