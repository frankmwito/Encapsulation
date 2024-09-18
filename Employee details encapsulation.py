# Employee Details Encapsulation

class Employee:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position
        self.__salary = None  # Encapsulated attribute for salary
        
    # Setter method to assign salary
    def set_salary(self, salary):
        self.__salary = salary
    
    # Method to increase salary by a percentage
    def salary_increase(self, percentage):
        if self.__salary:
            self.__salary += self.__salary * (percentage / 100)
        return self.__salary
    
    # Getter method to get employee details
    def get_details(self):
        return f"Employee Details - Name: {self.name}, Age: {self.age}, Position: {self.position}, Salary: {self.__salary}"
    

# Creating an employee instance and setting details
employee1 = Employee(input("Enter the name of employee: "), int(input("Enter the age of employee: ")), input("Enter the position of employee: "))

# Setting the employee's salary
employee1.set_salary(float(input("Enter the salary of the employee: ")))

# Increasing the salary by a percentage
print(f"New salary after increase: {employee1.salary_increase(float(input('Enter the percentage increase for salary: ')))}")

# Displaying employee details
print(employee1.get_details())
