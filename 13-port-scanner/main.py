import socket
import sys
import time


def scan_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    timeout = 1
    s.settimeout(timeout)
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
    start_time = time.time()
    host = sys.argv[1]
    try:
        socket.gethostbyname(host)
    except socket.gaierror:
        print(f"Error: could not resolve host '{host}'")
        sys.exit()
    try:
        start_port = int(sys.argv[2])
        end_port = int(sys.argv[3])
        for port in range(start_port, end_port + 1):
            if scan_port(host, port):
                service = get_service(port)
                print(f"{port} {service} open")
        end_time = time.time()
        duration = end_time - start_time
        print(f"Scan completed in {duration:.2f} seconds")
    except ValueError:
        print("Error: Invalid port range")



if __name__ == "__main__":
    main()
