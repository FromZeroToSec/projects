import platform

def main():
    print(f"Python version: {platform.python_version()}")
    print(f"OS: {platform.system()}")
    print(f"Platform: {platform.platform()}")
    print(f"Processor: {platform.processor()}")
    print(f"Machine: {platform.machine()}")
    print(f"Version: {platform.version()}")
    print(f"Release: {platform.release()}")


if __name__ == "__main__":
    main()