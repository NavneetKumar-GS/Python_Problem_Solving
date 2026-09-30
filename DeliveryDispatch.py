# The Application Spec: Delivery Dispatch System
# 1. The Contract (Abstract Base Class)
# Create an abstract class DeliveryVehicle.

# It must have an abstract method called deliver(package_name).

# 2. The Concrete Implementations (Inheritance)
# Create two child classes: Drone and Van.

# Both must inherit from DeliveryVehicle.

# Both must implement deliver(package_name).

# Drone should print: "🚁 Drone flying to deliver: [package_name]"

# Van should print: "🚐 Van driving to deliver: [package_name]"

# 3. The Manager (Composition & Encapsulation)
# Create a DispatchCenter class.

# Encapsulation: It must have a private variable __deliveries_completed set to 0.

# Composition: It must have a list called fleet to hold vehicle objects.

# A method add_vehicle(vehicle: DeliveryVehicle) that adds a vehicle to the fleet.

# A method dispatch_all(packages) that takes a list of package strings. It should loop through the packages, assign each one to a vehicle in the fleet (just cycle through them), call that vehicle's .deliver() method, and increment the private __deliveries_completed variable.

# Use @property to create a getter that returns the total __deliveries_completed.

# 4. The Safety Net (Context Manager)
# Create a ShiftManager class with __enter__ and __exit__.

# __enter__ prints: "--- 🟢 Shift Started. Dispatch System Online ---"

# __exit__ prints: "--- 🔴 Shift Ended. System Offline ---". If a crash happens during the shift, it must catch the error, print "🚨 Emergency Logged: [error]", and return True to prevent the whole app from dying.

from abc import ABC, abstractmethod

class DeliveryVehicle(ABC):
    @abstractmethod
    def deliver(self, package_name):
        pass

class Drone(DeliveryVehicle):
    def deliver(self, package_name):
        print(f"🚁 Drone flying to deliver: {package_name}")

class Van(DeliveryVehicle):
    def deliver(self, package_name):
        print(f"🚐 Van driving to deliver: {package_name}")

class DispatchCenter:
    def __init__(self):

        self.__completed_deliveries = 0
        self.fleet = []

    @property
    def deliveries_completed(self):
        return self.__completed_deliveries

    def add_vehicle(self, vehicle: DeliveryVehicle):
        self.fleet.append(vehicle)

    def dispatch_all(self, packages):
        if not self.fleet:
            print("No vehicles to dispatch")
            return

        fleet_size = len(self.fleet)

        for i in range(len(packages)):
           
            vehicle_index = i % fleet_size
            current_vehicle = self.fleet[vehicle_index]

       
            current_vehicle.deliver(packages[i])

 
            self.__completed_deliveries += 1

class ShiftManager:
    def __enter__(self):
        print("--- 🟢 Shift Started. Dispatch System Online ---")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("--- 🔴 Shift Ended. System Offline ---")
        
        if exc_type is not None:
            print(f"Error logged: {exc_val}")
            return True

# --- Testing ---
center = DispatchCenter()
center.add_vehicle(Drone())
center.add_vehicle(Van())

with ShiftManager():
    center.dispatch_all(["Medical Supplies", "Laptop", "Groceries", "Documents"])
    print(f"Total Deliveries Today: {center.deliveries_completed}")
    raise RuntimeError("GPS Server went down!")

print("\nSystem safely rebooting for the next day. The script did not crash.\n")

print("--- SCENARIO 1: Calm Day, No Crashes ---")
center1 = DispatchCenter()
center1.add_vehicle(Van()) 

with ShiftManager():
    center1.dispatch_all(["Just one pizza"])
    print(f"Total Deliveries Today: {center1.deliveries_completed}")

print("\n--- SCENARIO 2: High Traffic ---")
center2 = DispatchCenter()
center2.add_vehicle(Drone())
center2.add_vehicle(Van()) 
center2.add_vehicle(Drone())

with ShiftManager():
    center2.dispatch_all(["Pkg A", "Pkg B", "Pkg C", "Pkg D", "Pkg E", "Pkg F", "Pkg G"])
    print(f"Total Deliveries Today: {center2.deliveries_completed}")