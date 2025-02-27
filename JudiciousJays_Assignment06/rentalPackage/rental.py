# File Name : rental.py
# Student Name: Zoha Iqbal
# email: iqbalza@mao;.uc.edu
# Assignment Number: Assignment 06  
# Due Date: 02/26/25
# Course #/Section:  4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment: we are doing the tasks required for the class 

# Brief Description of what this module does is to fork, commit and push sucessfully
# Citations: N/A

# Anything else that's relevant: N/A

 
class Rental:
    def __init__(self, car, customer, rental_duration):
        self._car = car
        self._customer = customer
        self._rental_duration = rental_duration  # in days
        self._total_cost = 0

    def __str__(self):
        return (f"Rental({self._customer.name} renting {self._car._make} {self._car._model} "
                f"for {self._rental_duration} days, Total Cost: ${self._total_cost})")

    def __repr__(self):
        return f"Rental({repr(self._customer)}, {repr(self._car)}, {self._rental_duration})"

    # Property for rental_duration with getter and setter
    @property
    def rental_duration(self):
        return self._rental_duration

    @rental_duration.setter
    def rental_duration(self, days):
        self._rental_duration = days

    # Property for total_cost with getter and setter
    @property
    def total_cost(self):
        return self._total_cost

    @total_cost.setter
    def total_cost(self, cost):
        self._total_cost = cost

    # Method to start the rental process: rents the car and calculates total cost
    def start_rental(self):
        rental_message = self._car.rent()
        self._total_cost = self.calculate_total()
        return rental_message

    # Method to calculate the total cost based on rental duration and car rental price
    def calculate_total(self):
        return self._rental_duration * self._car.rental_price

    # Method to end the rental process by returning the car
    def end_rental(self):
        return self._car.return_car()
