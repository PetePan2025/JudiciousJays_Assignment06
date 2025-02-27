# File Name : customer.py
# Student Name: Uruz Bidiwala
# email:  bidiwaur@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date:  02/27/25
# Course #/Section: IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment: Group assignment

# Brief Description of what this module does. Demonstrate knowledge on Object-Oriented Programming
# Citations: 

# Anything else that's relevant:

class Customer:
    def __init__(self, name, license_number):
        self._name = name
        self._license_number = license_number

    def __str__(self):
        return f"Customer: {self._name}, License: {self._license_number}"

    def __repr__(self):
        return f"Customer('{self._name}', '{self._license_number}')"

    # Property for name with getter and setter
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    # Property for license_number with getter and setter
    @property
    def license_number(self):
        return self._license_number

    @license_number.setter
    def license_number(self, new_license):
        self._license_number = new_license

    # A method to greet the customer
    def greet(self):
        return f"Hello, my name is {self._name} and I'm ready to rent a car!"
