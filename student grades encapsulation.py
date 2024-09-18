# Student grades encapsulation

class Student:
    def __init__(self, name):
        self.name = name
        self.__grades = []  # Private attribute for grades
        
    # Method to add grades for multiple subjects
    def add_grades(self, number_of_subjects):
        for i in range(number_of_subjects):
            grade = float(input(f"Enter grade for subject {i+1}: "))
            self.__grades.append(grade)
        return f"Grades added: {self.__grades}"
    
    # Method to retrieve all grades (encapsulated access)
    def get_grades(self):
        return self.__grades
    
    # Method to calculate the average of the grades
    def calculate_average(self):
        if len(self.__grades) == 0:
            return "No grades available to calculate average"
        average = sum(self.__grades) / len(self.__grades)
        return f"Average grade: {average}"
        
        
# Create a Student instance and add grades
student1 = Student(input("Enter student's name: "))

# Adding grades to the student
print(student1.add_grades(int(input("Enter the number of subjects: "))))

# Getting the grades
print(f"Grades for {student1.name}: {student1.get_grades()}")

# Calculating the average grade
print(student1.calculate_average())
