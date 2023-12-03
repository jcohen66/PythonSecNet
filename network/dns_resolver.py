import dns.resolver
"""
Using the resolve() method to obtain a list of IP addresses for
many host domains with the dns.resolver submodule.
"""

hosts = ["python.org", "google.com", "facebook.com", "youtube.com", "yahoo.com", "baidu.com", "wikipedia.org",]
for host in hosts:
    print(host, ":", end=" ")
    try:
        answers = dns.resolver.query(host, "A")
        for answer in answers:
            print(answer, end=" ")
    except Exception as e:
        print(e)
    print()