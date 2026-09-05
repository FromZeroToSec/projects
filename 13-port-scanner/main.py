import socket
import sys


host = sys.argv[1]# get host from command line arguments
for port in range(int(sys.argv[2]), int(sys.argv[3]) + 1) :# loop through ports
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# create socket
    result = s.connect_ex((host, port))# returns 0 if port is open
    s.close()
    if result == 0: # if port is open
        try:# find service
            service = socket.getservbyport(port, "tcp")# get service
        except OSError:# if service is not found
            service = "Unknown"
        print(f"{port} {service} open")
    else:
        print(f"{port} closed")
