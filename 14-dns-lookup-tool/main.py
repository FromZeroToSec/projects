import socket
import dns.resolver
import argparse


def resolve_domain(domain):
    """Resolve a domain name to its IPv4 address."""
    return socket.gethostbyname(domain)


def get_mx_record(domain):
    """Retrieve the MX (Mail Exchange) records for a domain."""
    mx_list = []
    for record in dns.resolver.resolve(domain, "MX"):
        mx_list.append(f"{record.preference} {record.exchange}")
    return mx_list


def get_ns_record(domain):
    """Retrieve the NS (Name Server) records for a domain."""
    ns_list = []
    for record in dns.resolver.resolve(domain, "NS"):
        ns_list.append(f"{record.target}")
    return ns_list


def main():
    """Parse CLI arguments and print A, MX, and NS records for a domain."""
    parser = argparse.ArgumentParser()
    parser.add_argument("domain")
    args = parser.parse_args()
    domain = args.domain

    # A record (IP resolution)
    try:
        ip_address = resolve_domain(domain)
        print(f"The IP address for {domain} is: {ip_address}")
    except socket.gaierror:
        print("Enter a valid domain name.")

    # MX record (mail servers)
    try:
        mx_records = get_mx_record(domain)
        for mx in mx_records:
            print(f"MX record: {mx}")
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        print(f"No MX records found for {domain}.")

    # NS record (name servers)
    try:
        ns_records = get_ns_record(domain)
        for ns in ns_records:
            print(f"NS record: {ns}")
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        print(f"No NS records found for {domain}.")


if __name__ == "__main__":
    main()