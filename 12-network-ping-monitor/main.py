import subprocess


def check_ping(address):
    """Check if an address is reachable by sending a single ping."""
    try:
        # timeout=5 prevents the script from waiting forever
        result = subprocess.run(["ping", "-c", "1", address], capture_output=True, text=True, timeout=5)
        return result.returncode == 0  # 0 means success
    except subprocess.TimeoutExpired:
        return False  # address did not respond in time


def main():
    address_list = []
    while True:
        address = input("Which address do you want to check? (press Enter to stop): ")
        if not address:  # empty input (Enter) stops the loop
            break
        address_list.append(address)

    for address in address_list:
        if check_ping(address):
            print(f"{address} is Available")
        else:
            print(f"{address} is Not available")


if __name__ == "__main__":
    main()