# port-scanner

A simple TCP port scanner written in Python, built to understand how tools like Nmap work under the hood.

## What it does

- Scans a range of ports on a given host using TCP connect scanning
- Identifies the standard service name for each open port (HTTP, SSH, etc.)
- Handles unreachable hosts and unresponsive ports without crashing (timeout + error handling)
- Reports total scan duration

## Usage

python3 main.py <host> <start_port> <end_port>

Example:

python3 main.py 127.0.0.1 1 1025

Output:

631 ipp open
5432 postgresql open
Scan completed in 0.45 seconds

## What this demonstrates

- Python's socket module (TCP connections, connect_ex, timeouts)
- Command-line argument handling (sys.argv)
- Error handling (socket.gaierror, ValueError)
- Code structured into functions with docstrings

## Notes

Only scan hosts you own or have explicit permission to test.
