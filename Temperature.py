# Advanced Encapsulation
# Build a Temperature class.

# 1.Store the temperature internally in Celsius using a mangled variable (__celsius).

# 2.Use the @property decorator to create a getter and setter for the temperature.

# 3.The setter must enforce logic: if the provided temperature is below absolute zero (-273.15 C), raise a ValueError immediately.

class Temperature:
    def __init__(self,temp):

        self.temperature = temp

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C)!")
        else:
            self.__temperature = value
    def __str__(self):
        return f"{self.__temperature} C"
        


temp = Temperature(-30)
print(temp)

temp.temperature = 40
print(temp.temperature)
        