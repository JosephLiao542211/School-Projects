import datetime
from datetime import timedelta

"""
-------------------------------------------------------
Hotel data structure
-------------------------------------------------------
Author:  Joseph Liao
ID:      20366481
Email: 22jl41@queensu.ca
Section: CISC121 Winter 2023
-------------------------------------------------------
"""

import datetime

class Hotel:
    def __init__(self, rn):
        # Initialize the hotel room number and availability status
        self.room_number = rn
        self.avaliablitystat = True

    def guest_check_in(self, some_guest):
        """
        Update the hotel room's guest and availability status
        based on the provided guest's check-out date.

        If the room is a Suite or TaylorSuite, set the available
        date to the day after the provided guest's check-out date.

        Parameters:
        -----------
        some_guest: Guest object
            The guest checking in to the hotel room.
        """
        self.guest = some_guest
        self.avaliablitystat = False

        # Set the available date based on the room type
        if isinstance(self, Suite):
            self.avaliable = some_guest.checkout + datetime.timedelta(days=1)
        elif isinstance(self, TaylorSuite):
            self.avaliable = some_guest.checkout + datetime.timedelta(days=2)
        else:
            self.avaliable = some_guest.checkout

class TaylorSuite(Hotel):
    def __init__(self, room_number):
        # Initialize the available date as a default value
        self.avaliable = datetime.date(1, 1, 1)
        super().__init__(room_number)

class Suite(Hotel):
    def __init__(self, room_number):
        # Initialize the available date as a default value
        self.avaliable = datetime.date(1,1,1)
        super().__init__(room_number)

class Standard(Hotel):
    def __init__(self, room_number):
        # Initialize the available date as a default value
        self.avaliable = datetime.date(1, 1, 1)
        super().__init__(room_number)

class Guest:
    def __init__(self, name, checkoutdate):
        # Initialize the guest's name, check-out date, service list, and bill
        self.name = name
        self.checkout = datetime.date(checkoutdate[0], checkoutdate[1], checkoutdate[2])
        self.service = []
        self.bill = 0

    def add_service(self, service):
        """
        Add a service to the guest's service list and update the bill.

        Parameters:
        -----------
        service: Service object
            The service being added to the guest's list.
        """
        self.service.append((service.name, service.cost))
        self.bill += service.cost

    def send_bill(self):
        """
        Print the guest's name, service list, and total bill.
        """
        print(f"Guest Name: {self.name}")
        print("Services:")
        for service in self.service:
            print(f"{service[0]}: ${service[1]}")
        print(f"Total Bill: ${self.bill}")

class Service:
    def __init__(self, name, cost):
        # Initialize the service's name and cost
        self.name = name
        self.cost = cost

