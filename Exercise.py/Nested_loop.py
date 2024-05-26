def nested_multiplication_tables(n, limit):
    for number in range(1, n + 1):  # Outer loop for different numbers
        print(f"\nMultiplication table for {number}:")
        for i in range(1, limit + 1):  # Inner loop for the multiplication table of each number
            print(f"{number} x {i} = {number * i}")

n = int(input("Enter the range of numbers for which you want to generate the multiplication tables: "))
limit = int(input("Enter the limit up to which you want the multiplication tables: "))
nested_multiplication_tables(n, limit)
