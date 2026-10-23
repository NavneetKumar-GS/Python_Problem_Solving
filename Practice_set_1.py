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


# 4.Write a program that will give you the sum of 3 digits
x,y,z=map(int,input().split())

sum= x+y+z

print(f"Sum of {x}+{y}+{z}= {sum}")


# 5.Write a program that will reverse a four digit number.Also it checks whether the reverse is true.

num = int(input("Enter the number: "))

reversed_num = int(str(num[::-1]))

is_palindrome = (num==reversed_num)

print(f"Original Number: {num}")
print(f"Reversed Number: {reversed_num}")
print(f"Is the reverse true (Palindrome)? {is_palindrome}")


# 6.Write a program that will tell whether the number entered by the user is odd or even.

num = int(input("Enter the number: "))


if num%2==0:
    print("{num} is even")
else:
    print(f"{num} is odd")

# 7.Write a program to find the euclidean distance between two coordinates.
import math
point_a, point_b = map(int, input().split())

distance = math.dist(point_a,point_b)

print(f"Euclidean distance is: {distance} ")
