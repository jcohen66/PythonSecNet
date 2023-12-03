import argparse
import dns.name

def main(domain1, domain2):
    domain1 = dns.name.from_text(domain1)
    domain2 = dns.name.from_text(domain2)
    print(f"{domain1} is a subdomain of {domain2}: {domain1.is_subdomain(domain2)}")
    print(f"{domain2} is a subdomain of {domain1}: {domain2.is_subdomain(domain1)}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Check 2 domains with dnsPython")
    parser.add_argument("--domain1", dest="domain1", required=True, action="store", default="python.org")
    parser.add_argument("--domain2", dest="domain2", required=True, action="store", default="docs.python.org")
    given_args = parser.parse_args()

    domain1 = given_args.domain1
    domain2 = given_args.domain2
    main(domain1, domain2)