import random

# Main game loop  restarts the game after each round
while True:
    secret_number = random.randint(1, 10)  # Generate a random number between 1 and 10
    attempts = 0

    # Attempt loop — max 5 tries per round
    while attempts < 5:
        user_guess = int(input("Choose a number between 1 and 10: "))
        attempts += 1

        if user_guess == secret_number:
            print("You win!")
            break
        elif user_guess > secret_number:
            print("Too high")
        elif user_guess < secret_number:
            print("Too low")
    else:
        print(f"You lose! The secret number was {secret_number}")

    # Ask player if they want to play again
    play_again = input("Play again? (y/n): ").lower()
    if play_again == "n":
        break