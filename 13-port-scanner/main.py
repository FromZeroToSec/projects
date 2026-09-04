import socket


host = "127.0.0.1"

for port in range(1,1025):
    #créer socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #tester connexion
    result = s.connect_ex((host, port))
    #fermer socket
    s.close()
    #si port ouvert:
    if result == 0:
        #chercher le service (try/except)
        try:
            service = socket.getservbyport(port, "tcp")
        except OSError:
            service = "Unknown"
    # afficher port + service + "open"
        print(f"{port} {service} open")
    #sinon:
    else:
        print(f"{port} closed")

