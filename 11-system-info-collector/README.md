# System Info Collector

A command-line tool that collects and displays system information: operating system details, CPU usage, RAM usage, and disk usage. Built as part of the [FromZeroToSec](https://github.com/FromZeroToSec) roadmap (Bloc 2 — Linux & Network).

## What it does

Running the script prints a full system report to the terminal, including:

- **OS info**: Python version, OS name, platform, processor, machine architecture, OS version and release
- **CPU**: current usage (%), physical core count, logical core count
- **Memory**: usage (%), total RAM (GB), available RAM (GB)
- **Disk**: usage (%), total disk space (GB), available disk space (GB)

## Installation

Clone the repo and move into the project folder:

```bash
git clone https://github.com/FromZeroToSec/projects.git
cd projects/11-system-info-collector
```

Create and activate a virtual environment:

```bash
python3 -m venv env
source env/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the script:

```bash
python3 main.py
```

Example output:

```
Python version: 3.12.3
OS: Linux
Platform: Linux-7.0.0-28-generic-x86_64-with-glibc2.39
Processor: x86_64
Machine: x86_64
Version: #28~24.04.1-Ubuntu SMP PREEMPT_DYNAMIC Wed Jul 1 15:50:57 UTC 2
Release: 7.0.0-28-generic
CPU usage: 6.1
Physical cores: 8
Logical cores: 12
Memory usage: 47.3%
Total RAM (GB): 15.99
Available RAM (GB): 8.42
Disk usage: 62.0%
Total disk space (GB): 250.0
Available disk space (GB): 95.0
```

## What this demonstrates

- Reading system-level information in Python using the standard `platform` module
- Using a third-party library (`psutil`) to query live CPU, memory, and disk metrics
- Managing dependencies properly with a virtual environment and `requirements.txt`
- Converting raw byte values into human-readable units (GB)
- Clean function structure with a `main()` entry point guarded by `if __name__ == "__main__":`

## Tech stack

- Python 3
- [`psutil`](https://pypi.org/project/psutil/) — cross-platform system and process utilities
- `platform` — Python standard library
