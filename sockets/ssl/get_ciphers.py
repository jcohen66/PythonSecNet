import ssl

ciphers = ssl.SSLContext(ssl.PROTOCOL_TLSv1).get_ciphers()
for cipher in ciphers:
    print(f'{cipher["name"]} {cipher["protocol"]}')
