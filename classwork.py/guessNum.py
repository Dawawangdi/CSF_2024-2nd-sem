# Importing standard package for later use
import random

# Function to welcome the user
def welcome():
    print("Welcome to the Number Guessing Game!")

# Recursive function to play the guessing game
def guess_number(secret_num, attempts=3):
    print("You have", attempts, "attempts left.")
    guess = int(input("Guess the number (between 1 and 10): "))
    
    if guess == secret_num:
        print("Congratulations! You guessed the correct number!")
    elif attempts == 1:
        print("Sorry, you've used all your attempts. The correct number was:", secret_num)
    else:
        if guess < secret_num:
            print("Try a higher number.")
        else:
            print("Try a lower number.")
        guess_number(secret_num, attempts - 1)

# Calling a function for the execution
def main():
    # Generating a random number between 1 and 10
    secret_number = random.randint(1, 10)
    
    # Print memory address of the secret number
    print("Memory address of the secret number:", id(secret_number))
    
    # Welcome the user
    welcome()
    
    # Play the guessing game with 3 attempts
    guess_number(secret_number, 3)

if __name__ == "__main__":
    main()
