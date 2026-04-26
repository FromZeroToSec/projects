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

max_attempts = 5

def run_quiz():
    port = choice(list(PORTS.keys()))
    service = PORTS[port].lower()
    print(f"What service runs on port {port}?")
    return service, port


while True:
    service, port = run_quiz()
    attempts = 0

    while attempts < max_attempts:
        answer = input("Your answer: ").lower()
        if answer == service:
            print("🔥 You Win!")
            break
        else:
            attempts += 1
            remaining = max_attempts - attempts
            print(f"❌ Wrong! {remaining} attempt(s) left")
            if attempts == 2:
                print(f"The first letter of service is {service[0].upper()}")

    if attempts == max_attempts:
        print(f" You lose! The correct answer was: {service}")

    again = input("Play again? (y/n): ").lower()
    if again == "n":
        break