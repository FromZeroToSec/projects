import socket


host = "127.0.0.1"
for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((host, port))
    if result == 0:
        print(f"{port} open")
    else:
        print(f"{port} closed")
    s.close()

