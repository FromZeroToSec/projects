import socket


def resolve_domain(domain):
    return socket.gethostbyname(domain)


def main():
    try:
        domain = input("Enter a domain name: ")
        ip_address = resolve_domain(domain)
        print(f"The IP address for {domain} is: {ip_address}")
    except socket.gaierror:
        print("Enter a valid domain name.")


if __name__ == "__main__":
    main()