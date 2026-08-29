import subprocess


def check_ping(address):
    """check if an address is reachable"""
    result = subprocess.run(["ping", "-c", "1", address], capture_output=True, text=True)
    return result.returncode == 0 # if the return code is 0, the address is reachable


def main():
    address_list = []
    while True:
        address = input("Which address do you want to check? (press Enter to stop): ")
        if not address:
            break
        address_list.append(address)
    for address in address_list:
        if check_ping(address):
            print(f"{address} is Available")
        else:
            print(f"{address} is Not available")


if __name__ == "__main__":
    main()
