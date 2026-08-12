from datetime import datetime
import os

LOG_FILE = "app.log"
BACKUP_FILE = "app.log.old"
MAX_LOG_SIZE = 1000
ALLOWED_LEVELS = ["INFO", "WARNING", "ERROR"]


def write_log(message, level):
    """Write a log entry to the log file with the given level.

    Args:
        message (str): The log message to write.
        level (str): The log level, one of "INFO", "WARNING", "ERROR".
    """
    if level not in ALLOWED_LEVELS:
        print(f'Invalid log level: {level}')
        return

    rotate_log()

    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(LOG_FILE, 'a') as f:
            f.write(f'[{formatted_time}] [{level}] {message}\n')
    except OSError as e:
        print(f'Failed to write log: {e}')


def get_logs_size():
    """Return the current size of the log file in bytes.

    Returns 0 if the log file does not exist.
    """
    if not os.path.exists(LOG_FILE):
        return 0
    return os.path.getsize(LOG_FILE)


def rotate_log():
    """Rotate the log file to a backup when it exceeds the maximum size."""
    if get_logs_size() > MAX_LOG_SIZE:
        if os.path.exists(BACKUP_FILE):
            os.remove(BACKUP_FILE)
        os.rename(LOG_FILE, BACKUP_FILE)


def main():
    """Run the demo logging sequence."""
    write_log("Server started", "INFO")
    write_log("High memory usage detected", "WARNING")
    write_log("Database connection failed", "ERROR")
    write_log("Invalid entry test", "BLABLA")


if __name__ == '__main__':
    main()

