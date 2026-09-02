import random

# Main game loop — restarts after each round
while True:
    print("The Mystery Number Game")
    secret_number = random.randint(1, 100)  # Generate a random number between 1 and 100
    attempts = 0
    remaining = 5

    # Attempt loop — max 5 tries per round
    while attempts < 5:
        try:
            guess = int(input("Guess the number: "))
            attempts += 1
            remaining -= 1

            if secret_number == guess:
                print(f"Well done! The mystery number was {secret_number}!")
                print(f"You found it in {attempts} attempt(s)!")
                break
            elif secret_number > guess:
                print(f"The mystery number is greater than {guess}.")
                print(f"You have {remaining} attempt(s) left.")
            elif secret_number < guess:
                print(f"The mystery number is less than {guess}.")
                print(f"You have {remaining} attempt(s) left.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print(f"You lost! The mystery number was {secret_number}.")

    # Ask player if they want to play again
    play_again = input("Play again? (y/n): ").lower()
    if play_again == "n":
        break