# Composition over Inheritance (System Design)
# Build a simulation of an EV Charging Station (since you are interested in tech infrastructure).

# 1.Create an EVCharger class. It has an id (int) and a status (string: "Available", "Charging", "Offline").

# 2.Create a ChargingStation class. It does not inherit from EVCharger. Instead, it has a chargers attribute which is a list containing EVCharger objects (this is Composition).

# 3.Add a method add_charger(charger) to the station.

# 4.Add a method get_available_chargers() to the station that returns a list of only the chargers whose status is "Available".

