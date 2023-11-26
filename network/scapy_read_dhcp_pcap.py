from scapy.all import *
from collections import Counter
from prettytable import PrettyTable
"""
store the source IP in a list. To do that, we will
loop through the packets using a try/except block as not every packet will have the information
we want. Now that we have a list of IPs from the packets, we will use a counter to create a count.
Next, we will loop through the data and add them to the table from highest to lowest.
"""

# tell scapy to read all of the packets in the PCAP to a list
packets = rdpcap('packets_DHCP.cap')
srcIP = []
for packet in packets:
    if IP in packet:
        try:
            # Packets in scapy have elements; we will only be dealing with packets’ IP data
            srcIP.append(packet[IP].src)
        except:
            pass
counter = Counter()
for ip in srcIP:
    counter[ip] += 1
table = PrettyTable(["IP", "Count"])
for ip, count in counter.most_common():
    table.add_row([ip, count])
print(table)
