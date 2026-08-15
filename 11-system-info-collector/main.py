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



if __name__ == "__main__":
    main()