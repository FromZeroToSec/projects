from datetime import datetime
import os


def write_log(message, level):
    """Write a log entry to the log file with the given level.

    Args:
        message (str): The log message to write.
        level (str): The log level, one of "INFO", "WARNING", "ERROR".
    """
    rotate_log()
    allowed_levels = ["INFO", "WARNING", "ERROR"]
    if level in allowed_levels:
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        with open('app.log', 'a') as f:
            f.write(f'[{formatted_time}] [{level}] {message}\n')
    else:
        print('Invalid log level')


def get_logs_size():
    """Return the current size of the log file in bytes."""
    size = os.path.getsize('app.log')
    return size


def rotate_log():
    """Rotate the log file if it exceeds the maximum size."""
    if os.path.exists('app.log'):
        if get_logs_size() > 1000:
            os.rename("app.log", "app.log.old")


def main():
    """Run the demo logging sequence."""
    write_log("Server started", "INFO")
    write_log("High memory usage detected", "WARNING")
    write_log("Database connection failed", "ERROR")
    write_log("Invalid entry test", "BLABLA")


if __name__ == '__main__':
    main()

