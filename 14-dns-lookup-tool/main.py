import socket
import dns.resolver
import argparse

def resolve_domain(domain):
    return socket.gethostbyname(domain)


def get_mx_record(domain):
    mx_list = []
    for record in dns.resolver.resolve(domain, "MX"):
        mx_list.append(f"{record.preference} {record.exchange}")
    return mx_list


def get_ns_record(domain):
    ns_list = []
    for record in dns.resolver.resolve(domain, "NS"):
        ns_list.append(f"{record.target}")
    return ns_list


def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("domain")
        args = parser.parse_args()
        domain = args.domain
        ip_address = resolve_domain(domain)
        print(f"The IP address for {domain} is: {ip_address}")
    except socket.gaierror:
        print("Enter a valid domain name.")
    try:
        mx_records = get_mx_record(domain)
        for mx in mx_records:
            print(f"MX record: {mx}")
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        print(f"No MX records found for {domain}.")
    try:
        ns_records = get_ns_record(domain)
        for ns in ns_records:
            print(f"NS record: {ns}")
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        print(f"No NS records found for {domain}.")



if __name__ == "__main__":
    main()