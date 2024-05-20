
##MULTIPLICATION TABLE WITH LOOPS

# Prompt user for the number and limit
number = int(input("Enter the number for the multiplication table: "))
limit = int(input("Enter the limit up to which you want the table generated: "))

# Print the header
print(f"Multiplication table for {number} up to {limit}:")

# Generate and print the multiplication table
for i in range(1, limit + 1):
    print(f"{number} x {i} = {number * i}")


