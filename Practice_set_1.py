# 1.User will input (3ages).Find the oldest one
x,y,z = map(int, input("Enter the age: ").split())

if x>y:
    print(f"{x} is the oldest")
elif y>z:
    print(f"{y} is the oldest")
else:
    print(f"{z} is the oldest")



# 2.Write a program that will convert celsius value to fahrenheit
c = int(input("Enter the temp(C) = "))

fahrenheit = (c*9/5)+ 32
print(f"{c} celsius = {fahrenheit} Fahrenheit  ")


# 3.User will input (2numbers).Write a program to swap the numbers
x,y = map(int ,input().split())

x,y = y,x
print(f"x = {x}, y = {y}")
