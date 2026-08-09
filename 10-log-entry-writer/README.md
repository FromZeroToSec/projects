# Log Entry Writer

A simple Python logging system that writes timestamped log entries to a file, validates log levels, and automatically rotates the log file when it exceeds a size limit.

## Features

- Write log entries with automatic timestamp
- Validate log level (`INFO`, `WARNING`, `ERROR`) before writing
- Reject invalid log levels without corrupting the log file
- Automatic log rotation when `app.log` exceeds 1000 bytes
- Rotation preserves old logs by renaming the file (`app.log` → `app.log.old`)

## Usage

Run the script directly:

```bash
python3 main.py
```

By default, `main()` demonstrates the core features:

```python
write_log("Server started", "INFO")
write_log("High memory usage detected", "WARNING")
write_log("Database connection failed", "ERROR")
write_log("Invalid entry test", "BLABLA")  # rejected, invalid level
```

To use the logger in your own code:

```python
from main import write_log

write_log("Your message here", "INFO")
```

## Example output (`app.log`)
