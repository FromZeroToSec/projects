from random import choice



PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    1433: "MSSQL",
    1521: "Oracle",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    6379: "Redis",
    8080: "HTTP-alt",
    8443: "HTTPS-alt",
    27017: "MongoDB",
    2375: "Docker",
    2376: "Docker-TLS",
    5000: "Flask",
    9200: "Elasticsearch",
    5601: "Kibana",
    22222: "SSH-alt",
}

attempts = 0
max_attempts = 5

def run_quiz():
    port = choice(list(PORTS.keys()))
    service = PORTS[port]
        
    print(f"What service runs on port {port}?")
    answer = input("Your answer: ")
    return service, answer , port


service, answer , port = run_quiz()
while True:
    attempts = 0
    while attempts < max_attempts:
        if service == answer:
            print("You Win ! ")
            again = input(f"Play again? (y/n): ").lower()
            if again == "n":
                break
        else:
            attempts +=1
            remaining = max_attempts - attempts
            print(f"You have {remaining} attempt(s) left")

            if remaining == 0:
                print(f"You lose! The correct answer was {port}")
                again = input("Play again? (y/n): ").lower()
                if again == "n":
                    break
    if again == "n":
        break
    