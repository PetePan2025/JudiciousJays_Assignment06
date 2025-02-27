# File Name : main.py
# Student Name: Peter Phan
# email:  phanpv@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date:   2/27/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Modeling something in the real world using classes

# Brief Description of what this module does. Demonstrate knowledge on Object-Oriented Programming
# Citations: 
# Anything else that's relevant:

from Car_package.Car_class import *
from customer_package.customer import *
from rentalPackage.rental import *

if __name__ == "__main__":
    # Simulate renting a car online
    car1 = Car("Toyota", "Camry", 2022, 30)
    car1._is_available = "Available"
    car2 = Car("Honda", "Accord", 2020, 30)
    car2._is_available = "Not Available"
    car3 = Car("Ford", "Edge", 2006, 40)
    car3._is_available = "Available"
    
    customerOne = Customer("Bob Hill", "ABC12345")
    print(customerOne.greet())
    
    print(" ")
    # Checks Website
    print("Car 1 availability:", car1._is_available)
    print("Car 2 availability:", car2._is_available)
    print("Car 3 availability:", car3._is_available)

    print(" ")
    # Chose Car 1
    print("Car 1:", car1)

    print(" ")
    # Rental Details
    rental1 = Rental(car1, customerOne, 7)
    rental1._total_cost = 210
    print(rental1)

    print(" ")
    # Car availability update to "Not Available"
    car1._is_available = "Not Available"
    print("Car 1 availability:", car1._is_available)
    print("Car 2 availability:", car2._is_available)
    print("Car 3 availability:", car3._is_available)
    print(" ")

    print("Several Days Later.....")
    print(" ")
    # Return Car
    print(customerOne.name, "has returned Car 1:", car1._year, car1._make, car1._model)

    print(" ")
    # Car availability update to "Available"
    car1._is_available = "Available"
    print("Car 1 availability:", car1._is_available)
    print("Car 2 availability:", car2._is_available)
    print("Car 3 availability:", car3._is_available)
    print(" ")







