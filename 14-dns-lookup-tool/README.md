# dns-lookup-tool

A command-line DNS reconnaissance tool that resolves a domain's IP address (A record) and retrieves its MX (mail) and NS (name server) records.

## Features

- Resolve a domain to its IPv4 address
- Retrieve MX records (mail servers) with priority
- Retrieve NS records (authoritative name servers)
- Graceful error handling for invalid or non-existent domains

## Installation

```bash
git clone https://github.com/FromZeroToSec/projects.git
cd projects/14-dns-lookup-tool
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python3 main.py <domain>
```

Example:

```bash
python3 main.py google.com
```

Output:

```
The IP address for google.com is: 142.250.75.14
MX record: 10 smtp.google.com.
NS record: ns1.google.com.
NS record: ns2.google.com.
NS record: ns3.google.com.
NS record: ns4.google.com.
```

## What this demonstrates

- Use of Python's `socket` module for basic DNS resolution (A records)
- Use of `dnspython` for typed DNS queries (MX, NS)
- Command-line argument parsing with `argparse`
- Exception handling for common DNS failure cases (`socket.gaierror`, `dns.resolver.NoAnswer`, `dns.resolver.NXDOMAIN`)
- Clean separation of concerns: one function per lookup type, orchestrated in `main()`

## Requirements

- Python 3
- [dnspython](https://pypi.org/project/dnspython/)
