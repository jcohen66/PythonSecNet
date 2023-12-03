import dns.resolver
import sys

"""
Record Types:
• AAAA record: This is an IP address record, which is used to find the IP of the computer
connected to the domain. It is conceptually like the A record but specifies only the IPv6
address of the server instead of the IP.

• NS record: The Name Server (NS) record provides information about which server is
authoritative for the given domain, that is, which server has the actual DNS records. Multiple
NS records are possible for a domain, including primary and backup name servers.

• MX records: MX stands for mail exchanger record, which is a resource record that specifies
the mail server that is responsible for accepting emails on behalf of the domain. It
has preference values according to the prioritization of mail if multiple mail servers are
present for load balancing and redundancy.

• SOA records: SOA stands for Start of Authority, which is a type of resource record that
contains information about the administration of the zone, especially related to zone
transfers defined by the zone administrator.

• CNAME record: CNAME stands for canonical name record, which is used to map the
domain name as an alias for the other domain. It always points to another domain and
never directly points to an IP.

• TXT record: These records contain the text information of the sources that are outside the
domain. TXT records can be used for various purposes, for example, Google uses them to
verify domain ownership and ensure email security.
This module allows operations to query records against DNS servers.

dnsPthon is a DNS toolkit for Python. It supports almost all record types.

The information that we can obtain for a specific domain is as follows:
    • Records for mail servers: response_MX = dns.resolver.query('domain','MX')
    • Records for name servers: response_NS = dns.resolver.query('domain','NS')
    • Records for IPV4 addresses: response_ipv4 = dns.resolver.query('domain','A')
    • Records for IPV6 addresses: response_ipv6 = dns.resolver.query('domain','AAAA')
"""
def main(domain):
    records = ["A", "AAAA", "CNAME", "MX", "NS", "PTR", "SOA", "TXT"]
    for record in records:
        try:
            answers = dns.resolver.resolve(domain, record)
            print(f"\nRecord response: {record}")
            print("--------------------")
            for answer in answers:
                print(answer)
        except Exception as e:
            print(f"Cannot resolve query for record {record}")
            print(f"Error for obtaining record information: {e}")

if __name__ == '__main__':
    try:
        domain = "python.org"
        main(domain)
    except KeyboardInterrupt:
        print("Interrupted by user...")
        sys.exit(0)