from abc import ABC, abstractmethod
from ride import RideRequest, RideMatching
class User(ABC):
    def __init__(self, name, email, nid) -> None:
        self.name = name
        self.email = email
        self.nid = nid
        self.wallet = 0
        
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError


class Rider(User):
    def __init__(self, name, email, nid, current_location, initial_amount) -> None:
        super().__init__(name, email, nid)
        self.current_ride = None
        self.wallet = initial_amount
        self.current_location = current_location
    
    def display_profile(self):
        print(f"Rider : {self.name} and email {self.email}")
    
    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount
        else:
            print("Amount less than 0")
    
    def update_location(self, current_location):
        self.current_location = current_location
    
    def request_ride(self, ride_sharing, destination, vehicle_type):
        ride_request = RideRequest(self, destination)
        ride_matching = RideMatching(ride_sharing.drivers)
        ride = ride_matching.find_driver(ride_request, vehicle_type)
        ride.rider = self
        self.current_ride = ride
        print("YAY!! We got a ride")
    
    def show_current_ride(self):
        print("Ride Details!!")
        print(f"Rider : {self.name}")
        print(f"Driver : {self.current_ride.driver.name}")
        print(f"Seleted Car : {self.current_ride.vehicle.vehicle_type}")
        print(f"Start Location : {self.current_ride.start_location}")
        print(f"End Location : {self.current_ride.end_location}")
        print(f"Total Cost : {self.current_ride.estimated_fare}")
        


# Dhakar Rampura - tumi
# Dhakar Malibag - Driver
# Dhakar rampura bajar - Driver 

# rampura --> mouchak 20
class Driver(User):
    def __init__(self, name, email, nid, current_location) -> None:
        super().__init__(name, email, nid) 
        self.current_location = current_location
        self.wallet = 0
    
    def display_profile(self):
        print(f"Driver Name : {self.name}")
    
    def accept_ride(self, ride):
        ride.start_ride()
        ride.set_driver(self) # driver er object 
    
    def reach_destination(self, ride):
        ride.end_ride()
    