import ssl
address = ('www.python.org', 443)
certificate = ssl.get_server_certificate(address)
print(certificate)