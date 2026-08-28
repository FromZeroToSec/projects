import subprocess


def check_ping(address):
    """check if an address is reachable"""
    result = subprocess.run(["ping", "-c", "1", address], capture_output=True, text=True)
    return result.returncode == 0 # if the return code is 0, the address is reachable

def main():
    address = input("Which address do you want to check? ")
    if check_ping(address):
        print("Available")
    else:
        print("Not available")

if __name__ == "__main__":
    main()