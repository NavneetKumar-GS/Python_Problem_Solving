# Build a base class called Employee and a child class called Manager.

# 1.Employee has an __init__ taking name and base_salary.

# 2.Employee has a method calculate_pay() which simply returns the base_salary.

# 3.Manager inherits from Employee but its __init__ also takes a bonus amount.

# 4.Override calculate_pay() in the Manager class so it returns base_salary + bonus. Use the super() function in your constructor.


class Employee:

    def __init__(self,name,salary):

        self.employee_name = name
        self.base_salary= salary

    def calculate_pay(self):
        print(f"Employee {self.employee_name} salary is {self.base_salary} ")

class Manger(Employee):

    def __init__(self,bonus,name,salary):

        super().__init__(name,salary)
        self.bonus_salary = bonus

    def calculate_pay(self):
        return self.bonus_salary + self.base_salary


mgr = Manger(800,"Rohan",1000)
print(f"{mgr.employee_name}'s,Total pay:${mgr.calculate_pay()}")