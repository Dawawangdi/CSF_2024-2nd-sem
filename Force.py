#condition type
print("F= ma *2nt law")
#determining the missing value
print("select the missing value: ")
print ("1.Mass(m)")
print ("2.acceleration(a)")
print ("3.Force(F)")
missing_value_choice = input ("Enter the option number for the missing value: ")

#user input
if missing_value_choice == "1":
    a = float (input("Enter acceleration(a): "))
    F = float (input ("Enter force(F): "))
    m = F/a
    print(f"mass (m)= {m}")
elif missing_value_choice =="2":
    m = float(input("Enter mass (m)): "))
    F = float(input("Enter force(F): "))
    a = F/m
    print(f"acceleeation(a): {a}")
elif missing_value_choice == "3":
    m = float(input("Enter mass (m)): "))
    a = float(input("Enter acceleration(a): "))
    F = m*a
    print(f"Force (F): (F)")

    print(f"acceleeation(a): {F}")

else :
    print("Entered number is invaild.")
