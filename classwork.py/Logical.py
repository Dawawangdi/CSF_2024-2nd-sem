

# Example 1: AND operator
x = 5
print(x < 3 and x > 10)  # False, because neither condition is true
y = 12
print(y > 10 and y % 2 == 0)  # True, because both conditions are true

# Example 2: OR operator
x = 5
print(x < 3 or x > 10)  # False, because neither condition is true
y = 12
print(y > 10 or y % 5 == 0)  # True, because the first condition is true

# Example 3: NOT operator
x = 5
print(not (x > 3 and x < 10))  # False, because the inner expression is True
y = 12
print(not (y > 10 and y % 5 == 0))  # True, because the inner expression is False



# Experiment with different values and conditions
x = 8  # golden number
guessing_number = input("Guess a number from 1 to 15.\nYou can pick any two numbers.\n")
number_chosen_one = int(input("First choice: "))
number_chosen_two = int(input("Second choice: "))

if number_chosen_one == x or number_chosen_two == x:
    print("Congratulations! You guessed the golden number!")
else:
    print("Sorry, try again.")




# Exercise: Determine if a person is eligible for a discount on a movie ticket
# based on their age and whether they are a student or not.

# Ask the user to input their age
age = int(input("Enter your age: "))

# Ask the user to input whether they are a student or not
student_status = input("Are you a student? (yes/no): ").lower()

# Determine if the person is eligible for a discount
if age <= 12:
    eligible_for_discount = True
elif 13 <= age <= 18 and student_status == "yes":
    eligible_for_discount = True
else:
    eligible_for_discount = False

# Print a message indicating whether the person is eligible for a discount or not
if eligible_for_discount:
    print("You are eligible for a discount on your movie ticket!")
else:
    print("You are not eligible for a discount on your movie ticket.")
