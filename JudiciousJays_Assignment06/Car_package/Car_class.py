# File Name : Car_class.py
# Student Name: Saivamsi Reddy Amireddy
# email:  amiredsr@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date:   02/27/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Modeling something in the real world using classes

# Brief Description of what this module does. Class for Car in a Car Rental Process
# Citations: 



class Car:
    def __init__(self, make, model, year, rental_price):
        """
        Initialize a new car instance
        """
        self._make = make
        self._model = model
        self._year = year
        self._rental_price = rental_price
        self._is_available = True

  
    def rental_price(self):
        """
        Get rental price per day
        """
        return self._rental_price
    

    def rental_price(self, price):
        """
        Set rental price per day
        """
        if price > 0:
            self._rental_price = price
        else:
            raise ValueError("Price must be greater than zero")

   
    def car_availability(self):
        """
        Car availability status
        """
        self._is_available = not self._is_available
        return self._is_available

    def __str__(self):
        """
        String representation of Car
        """
        return f"{self._year} {self._make} {self._model} - ${self._rental_price}/day"




