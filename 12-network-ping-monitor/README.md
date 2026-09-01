# Network Ping Monitor

A command-line tool that checks whether one or more network addresses are reachable, using Python's `subprocess` module to run the system `ping` command. Built as part of the [FromZeroToSec](https://github.com/FromZeroToSec) roadmap (Bloc 2 — Linux & Network).

## What it does

The script asks the user for one or more addresses (IP addresses or domain names), then checks each one and prints a clear availability report.

- Sends a single ping per address (`-c 1`), enough to confirm reachability without flooding the network
- Uses a 5-second timeout so the script never hangs on an unresponsive address
- Accepts multiple addresses in a row — just press Enter on an empty prompt to stop adding and run the checks

## Usage

Run the script:

```bash
python3 main.py
```

Example session:

```
Which address do you want to check? (press Enter to stop): 8.8.8.8
Which address do you want to check? (press Enter to stop): 1.1.1.1
Which address do you want to check? (press Enter to stop): 10.255.255.1
Which address do you want to check? (press Enter to stop): 
8.8.8.8 is Available
1.1.1.1 is Available
10.255.255.1 is Not available
```

## What this demonstrates

- Running system commands from Python with the `subprocess` module, without using `shell=True` (avoiding command injection risks)
- Reading a command's exit status (`returncode`) to determine success or failure
- Handling errors gracefully with `try`/`except`, including timeouts (`subprocess.TimeoutExpired`)
- Collecting a variable number of user inputs in a loop, with a clean exit condition
- Structuring reusable logic in a dedicated function (`check_ping`), separate from the `main()` flow

## Tech stack

- Python 3
- `subprocess` — Python standard library
