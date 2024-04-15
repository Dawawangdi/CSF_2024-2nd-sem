#import the random number
import random 
# grnerate a random nuber btw 1 to 10
secrect_num = random. randint(1,10)
max.attempts = 3,
def user_guess ():
    print("\n Welcom to guessing game.")
    print("you have {max_attempts} to uess the number between 1 to 10.")
def guess_recurssive(attempts_left):
    guess = int(input("\nGuess the number between 1 to 10:\n"))
    if guess == secrect_num:
        print("Congratulation you have guessed correctly.")
    else:
        print(f"wrong guess.Attempts left: {attempts_left-1}")
        if attempts_left >1:
            guess_recurssive(attempts_left -1)
        else:
            print(f"\nSorry, you couldn't guess the number right. The correct number was {secrect_num}")
    
user_guess()
guess_recurssive(max_attempts)
print(f"Memory address of secrect Number {secrect_num} is : {id(secrect_num)}")