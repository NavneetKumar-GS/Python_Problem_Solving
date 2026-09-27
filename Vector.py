# Build a Vector2D class to represent a mathematical vector (x, y).

# 1.The constructor takes x and y.

# 2. Overload the + operator (using the __add__ method) so you can add two Vector2D objects together (e.g., v3 = v1 + v2). Adding vectors means adding their respective x and y values.

# 3. Overload the string representation (using the __str__ method) so that printing the object outputs exact text in this format: <x: 5, y: 10>.


class Vector2d:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2d(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"<x: {self.x}, y: {self.y}>"

x = Vector2d(4, 5)
y = Vector2d(1, 5)

result = x+y
print(result)