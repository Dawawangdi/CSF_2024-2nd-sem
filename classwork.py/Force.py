# Print the title and explanation of Newton's 2nd law
print("F = ma (Newton's 2nd law)")

# Prompt the user to select which value is missing
print("Select the missing value:")
print("1. Mass (m)")
print("2. Acceleration (a)")
print("3. Force (F)")
missing_value_choice = input("Enter the option number for the missing value: ")

# Determine the missing value based on user input
if missing_value_choice == "1":
    # If the missing value is mass (m), prompt the user to enter acceleration (a) and force (F)
    a = float(input("Enter acceleration (a): "))
    F = float(input("Enter force (F): "))
    # Calculate mass using the formula m = F / a
    m = F / a
    # Print the calculated mass
    print(f"Mass (m) = {m}")
elif missing_value_choice == "2":
    # If the missing value is acceleration (a), prompt the user to enter mass (m) and force (F)
    m = float(input("Enter mass (m): "))
    F = float(input("Enter force (F): "))
    # Calculate acceleration using the formula a = F / m
    a = F / m
    # Print the calculated acceleration
    print(f"Acceleration (a) = {a}")
elif missing_value_choice == "3":
    # If the missing value is force (F), prompt the user to enter mass (m) and acceleration (a)
    m = float(input("Enter mass (m): "))
    a = float(input("Enter acceleration (a): "))
    # Calculate force using the formula F = m * a
    F = m * a
    # Print the calculated force
    print(f"Force (F) = {F}")
else:
    # If the input is invalid, print an error message
    print("Entered number is invalid.")
