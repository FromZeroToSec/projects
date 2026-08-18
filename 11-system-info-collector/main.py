import platform
import psutil


def main():
    print(f"Python version: {platform.python_version()}")
    print(f"OS: {platform.system()}")
    print(f"Platform: {platform.platform()}")
    print(f"Processor: {platform.processor()}")
    print(f"Machine: {platform.machine()}")
    print(f"Version: {platform.version()}")
    print(f"Release: {platform.release()}")
    print(f"CPU usage: {psutil.cpu_percent(interval=1)}")
    print(f"Physical cores: {psutil.cpu_count(logical=False)}")
    print(f"Logical cores: {psutil.cpu_count(logical=True)}")
    print(f"Memory usage: {psutil.virtual_memory().percent}%")
    print(f"Total RAM (GB): {round(psutil.virtual_memory().total / (1024 ** 3), 2)}")
    print(f"Available RAM (GB): {round(psutil.virtual_memory().available / (1024 ** 3), 2)}")
    print(f"Disk usage: {psutil.disk_usage('/').percent}%")
    print(f"Total disk space (GB): {round(psutil.disk_usage('/').total / (1024 ** 3), 2)}")
    print(f"Available disk space (GB): {round(psutil.disk_usage('/').free / (1024 ** 3), 2)}")


if __name__ == "__main__":
    main()