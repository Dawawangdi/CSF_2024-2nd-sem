class Exercise:
    def check_discount_eligibility(self):
        # Ask the user to input their age
        age = int(input("Enter your age: "))
        
        # Ask the user if they are a student
        is_student = input("Are you a student? (yes/no): ").lower()
        
        # Use logical operators to determine discount eligibility
        if age <= 12:
            print("You are eligible for a discount on the movie ticket.")
        elif 13 <= age <= 18 and is_student == 'yes':
            print("You are eligible for a discount on the movie ticket.")
        else:
            print("You are not eligible for a discount on the movie ticket.")

# Example usage:
exercise = Exercise()
exercise.check_discount_eligibility()
