##Exercise 3: Printing Numbers with Skipping and Breaking

# Print numbers from 1 to 9, skipping 3 in the inner loop and breaking when reaching 7
print("Printing numbers from 1 to 9 with skipping 3 and breaking at 7:")
for i in range(1, 10):
    if i == 7:
        break
    if i == 3:
        continue
    print(i)


