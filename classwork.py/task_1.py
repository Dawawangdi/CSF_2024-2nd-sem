Age = int (input ("Enter your age:"))
std = input ("Are you student? (yes/no):")

if Age <= 12 and (std =="yes"):
    print("You are eligible for a discount on ticket.")
elif Age <=18 and(Age>13 and std == "yes" ):
    print("you are  not eligible for a discount on ticket.")
    
elif Age > 12 and (std == "no"):
    print("sorry, you are  not eligible for a discount on ticket.")

else :
    print("Entered input is invaild")


