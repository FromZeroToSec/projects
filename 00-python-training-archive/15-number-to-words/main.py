ones = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}


tens = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
}


def number_to_word(number):
    """Convert an integer between 0 and 999 into its English word representation.

    Args:
        number (int): The number to convert, expected to be between 0 and 999.

    Returns:
        str: The number written out in English words (e.g. "forty-two").
    """
    if number >= 100:
        if number % 100 != 0:
            return f"{ones[number // 100]} hundred {number_to_word(number % 100)}"
        else:
            return f"{ones[number // 100]} hundred"
    elif number < 20:
        return ones[number]
    elif number % 10 == 0:
        return tens[number // 10]
    else:
        return f"{tens[number // 10]}-{ones[number % 10]}"


def main():
    """Main function to run the program. Asks the user for a number between 0 and 999,
    converts it to its English word representation, and then asks the user if they
    want to continue."""
    while True:
        try:
            number = int(input("Enter a number between 0 and 999: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if number < 0 or number > 999:
            print("Please enter a number between 0 and 999.")
            continue
        print(number_to_word(number))
        while True:
            choice = input("Do you want to continue? (y/n): ").lower()
            if choice == "y":
                break    # restart the loop
            elif choice == "n":
                return    # quit the program
            else:
                print("Invalid input. Please enter 'y' or 'n'.")


if __name__ == "__main__":
    main()