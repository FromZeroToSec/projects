import socket
import dns.resolver


def resolve_domain(domain):
    return socket.gethostbyname(domain)


def get_mx_record(domain):
    mx_list = []
    for record in dns.resolver.resolve(domain, "MX"):
        mx_list.append(f"{record.preference} {record.exchange}")
    return mx_list


def main():
    try:
        domain = input("Enter a domain name: ")
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



if __name__ == "__main__":
    main()