
# Guide for managing student grades

num_students = int(input("Enter the number of students: "))  # Prompt user for number of students
i = 1  # Initialize student counter

while i <= num_students:  # Loop over each student
    total_grade = 0  # Initialize total grade accumulator
    num_subjects = int(input(f"Enter the number of subjects for student {i}: "))  # Prompt for number of subjects
    
    for j in range(1, num_subjects + 1):  # Loop over each subject
        grade = float(input(f"Enter subject {j} grade for student {i}: "))  # Prompt for subject grade
        total_grade += grade  # Add grade to total
    
    average_grade = total_grade / num_subjects  # Calculate average grade
    print(f"Average grade for student {i}: {average_grade:.2f}")  # Print average grade with 2 decimal places
    
    i += 1  # Increment student counter







