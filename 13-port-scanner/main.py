import socket
import sys


def scan_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((host, port))
    s.close()
    if result == 0:
        return True
    else:
        return False


def get_service(port):
    try:
        service = socket.getservbyport(port, "tcp")
    except OSError:
        service = "Unknown"
    return service

def main():
    host = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])
    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            service = get_service(port)
            print(f"{port} {service} open")


if __name__ == "__main__":
    main()