# Composition over Inheritance (System Design)
# Build a simulation of an EV Charging Station (since you are interested in tech infrastructure).

# 1.Create an EVCharger class. It has an id (int) and a status (string: "Available", "Charging", "Offline").

# 2.Create a ChargingStation class. It does not inherit from EVCharger. Instead, it has a chargers attribute which is a list containing EVCharger objects (this is Composition).

# 3.Add a method add_charger(charger) to the station.

# 4.Add a method get_available_chargers() to the station that returns a list of only the chargers whose status is "Available".


class EVCharger:

    def __init__(self,charger_id:int, status:str = "Available"):
        self.charger_id = charger_id
        self.charger_status = status

    def __repr__(self):
        return f"EVCharger(ID={self.charger_id}, Status='{self.charger_status}')"

class ChargingStation:

    def __init__(self):

        self.chargers = []

    def add_charger(self,charger: EVCharger):
        self.chargers.append(charger)

    def get_available_chargers(self):
        return [charger for charger in self.chargers if charger.charger_status == "Available"]





charging_infra = ChargingStation()

charger_1 = EVCharger(charger_id=101, status="Available")
charger_2 = EVCharger(charger_id=102, status="Charging")
charger_3 = EVCharger(charger_id=103, status="Available")
charger_4 = EVCharger(charger_id=104, status="Offline")


charging_infra.add_charger(charger_1)
charging_infra.add_charger(charger_2)
charging_infra.add_charger(charger_3)
charging_infra.add_charger(charger_4)


available = charging_infra.get_available_chargers()

print(f"Available chargers: {available}")

        

