# multiplication table
def multiplication_table  (number, limit):
    print(f"Multiplication table for {number}: ")
    #for loop is being used
    for i in range (1, limit +1):
        print (f"{number} x {i} = {number * i}")

number = int(input("Enter the number for which you want to generate the multiplication table: "))
limit = int(input("Enter the limit up to which you want the multiplication table: "))
multiplication_table  (number, limit)
