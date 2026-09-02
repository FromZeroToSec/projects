# Number Stats — collects numbers and displays min, max, sum and average

def get_number():# Collect numbers from user
    """Collects numbers from user input until 'Q' is entered. Returns a list of integers."""
    numbers = []
    while True :
        user_input = input("Enter 'Q' to quit or Enter a number: ").upper()
        if user_input == "Q": 
                break
        try:    
            num = int(user_input)
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return numbers
        

def calculate_stats(numbers):
    """Calculates min, max, average and sum of a list of numbers. Returns a tuple of 4 values."""
    smallest = min(numbers)
    biggest = max(numbers)
    addition =sum(numbers)
    average = sum(numbers) / len(numbers)
    return smallest, biggest, average, addition# Calculate and display stats


def main():
    """Main function: collects numbers and displays statistics."""
    number = get_number()
    smallest, biggest, average, addition = calculate_stats(number)
    print(50 * "-")# Display stats
    print(f"Smallest number: {smallest}")
    print(f"Biggest number: {biggest}")
    print(f"Sum: {addition}")
    print(f"Average: {average}")


if __name__ == "__main__":
    main()