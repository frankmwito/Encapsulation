# Car Class with encapsulated attributes

class Car:
    def __init__(self, make, model, year, color):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__color = color
        self.__speed = 0  # Encapsulated attribute for speed, initialized at 0
        
    # Method to set car details
    def set_details(self):
        self.__make = input("Enter the make of the car: ")
        self.__model = input("Enter the model of the car: ")
        self.__year = input("Enter the year of the car: ")
        self.__color = input("Enter the color of the car: ")
    
    # Method to get car details
    def get_details(self):
        return f"Make: {self.__make}, Model: {self.__model}, Year: {self.__year}, Color: {self.__color}, Speed: {self.__speed} km/h"
    
    # Method to accelerate the car
    def accelerate_car(self, increase_speed):
        self.__speed += increase_speed
        return f"The car is now moving at {self.__speed} km/h"
    
    # Method to reduce the speed (brake)
    def reduce_speed(self, decrease_speed):
        self.__speed -= decrease_speed
        if self.__speed < 0:
            self.__speed = 0
        return f"The car is now moving at {self.__speed} km/h"
    

# Create a Car object and test the methods
car1 = Car("Toyota", "Corolla", 2020, "Red")

# Setting the car details
car1.set_details()

# Print car details
print(car1.get_details())

# Accelerate the car by a given speed
print(car1.accelerate_car(int(input("Enter speed to increase by: "))))

# Reduce the car speed
print(car1.reduce_speed(int(input("Enter speed to decrease by: "))))

        