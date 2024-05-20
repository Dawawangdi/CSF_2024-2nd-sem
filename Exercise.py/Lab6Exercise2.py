##Exercise 2: Right Triangle Pattern of Stars 


height = int(input("Enter the height of the triangle (number of rows): "))

# Print the pattern of stars
print("Pattern of stars in the shape of a right triangle:")
for i in range(1, height + 1):
    print("*" * i)

