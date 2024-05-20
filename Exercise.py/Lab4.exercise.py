# Initializing empty lists and dictionary to store student information
students_list = []  # List to store student names
students_dict = {}  # Dictionary to store student names as keys and their corresponding information (age and grade) as values

# Function to add student information
def add_student():
    name = input("Enter student's name: ")
    age = input("Enter student's age: ")
    grade = input("Enter student's grade: ")
    students_list.append(name)  # Add student name to the list
    students_dict[name] = {'age': age, 'grade': grade}  # Add student name as key and age and grade as values to the dictionary
    print("Student information added successfully!", students_dict.items())

# Function to search for a student
def search_student():
    name = input("Enter the name of the student to search or simply enter to skip: ")
    if name in students_dict:  # Check if student name exists in the dictionary
        print(f"Name: {name}, Age: {students_dict[name]['age']}, Grade: {students_dict[name]['grade']}")
    else:
        print("Student not found!")

# Function to remove a student
def remove_student():
    name = input("Enter the name of the student to remove or simply enter to skip: ")
    if name in students_dict:  # Check if student name exists in the dictionary
        del students_dict[name]  # Remove student from dictionary
        students_list.remove(name)  # Remove student from list
        print("Student removed successfully!")
    else:
        print("Student not found!")

# Test the system
add_student()  # Add a student
search_student()  # Search for a student
remove_student()  # Remove a student
