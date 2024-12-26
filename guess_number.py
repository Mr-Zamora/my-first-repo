# guess_number.py
# A simple game for practising GitHub basics
# Fork this repo, modify the game, and have fun!

import random

def guess_the_number():
    """A simple number-guessing game."""
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 10. Can you guess it?")
    
    number = random.randint(1, 10)  # Random number between 1 and 10
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

# Run the game if this script is executed directly
if __name__ == "__main__":
    guess_the_number()
