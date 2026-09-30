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