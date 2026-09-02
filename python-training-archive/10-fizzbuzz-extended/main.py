def fizzbuzz(number):
    """
    Returns the string representation of the given number:
    - "Fizz" if the number is divisible by 3 but not by 5
    - "Buzz" if the number is divisible by 5 but not by 3
    - "FizzBuzz" if the number is divisible by both 3 and 5
    - The number as a string otherwise
    """
    if number % 5 == 0  and number % 3 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)
    

def run_fizzbuzz(limit):
    """Prints the FizzBuzz sequence up to the given limit."""
    for number in range(1, limit + 1):
        print(fizzbuzz(number))


def main():
    """Main function to run the FizzBuzz program."""
    try:
        limit = int(input("Enter the limit: "))
        run_fizzbuzz(limit)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()