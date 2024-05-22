# Parent class 'Person' containing common attributes and methods
class Person:
    def __init__(self, name, age, cid_number):
        """Initialize common attributes for Person"""
        self.name = name
        self.age = age
        self.cid_number = cid_number

    def walk(self):
        """Simulate walking behavior"""
        print(f"{self.name} is walking.")

    def talk(self):
        """Simulate talking behavior"""
        print(f"{self.name} is talking.")

    def eat(self):
        """Simulate eating behavior"""
        print(f"{self.name} is eating.")

    def sleep(self):
        """Simulate sleeping behavior"""
        print(f"{self.name} is sleeping.")

# Child class 'Student' inheriting from 'Person'
class Student(Person):
    def __init__(self, name, age, cid_number, student_id, course, year, gpa):
        """Initialize Student specific attributes along with inherited attributes"""
        super().__init__(name, age, cid_number)  # Initialize parent class attributes
        self.student_id = student_id
        self.course = course
        self.year = year
        self.gpa = gpa

    def study(self):
        """Simulate studying behavior"""
        print(f"{self.name} is studying.")

    def attend_class(self):
        """Simulate attending class behavior"""
        print(f"{self.name} is attending class.")

    def write_exam(self):
        """Simulate writing exam behavior"""
        print(f"{self.name} is writing an exam.")

# Child class 'Teacher' inheriting from 'Person'
class Teacher(Person):
    def __init__(self, name, age, cid_number, subject, salary, department, designation):
        """Initialize Teacher specific attributes along with inherited attributes"""
        super().__init__(name, age, cid_number)  # Initialize parent class attributes
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation

    def teach(self):
        """Simulate teaching behavior"""
        print(f"{self.name} is teaching {self.subject}.")

    def grade_students(self):
        """Simulate grading students behavior"""
        print(f"{self.name} is grading students.")

    def attend_meeting(self):
        """Simulate attending meeting behavior"""
        print(f"{self.name} is attending a meeting.")

# Create instances to demonstrate inheritance and behaviors
student1 = Student("Alice", 20, "CID123", "S001", "Computer Science", 2, 3.8)
teacher1 = Teacher("Mr. Smith", 45, "CID456", "Mathematics", 50000, "Math Department", "Professor")

# Demonstrate Student behaviors
student1.walk()        # Inherited behavior
student1.study()       # Specific behavior
student1.attend_class()# Specific behavior

# Demonstrate Teacher behaviors
teacher1.walk()        # Inherited behavior
teacher1.teach()       # Specific behavior
teacher1.attend_meeting() # Specific behavior
