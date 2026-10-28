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


# 8.Write a program that take a user inputr of three angles and will find out whether it can form a triangle or not.

x,y,z = map(int, input().split())

angle_sum = x+y+z

if angle_sum == 180 and x>0 and y>0 and z>0:
    print("\nSuccess: These angles can form a valid triangle.")
else:
    if angle_sum != 180:
        print(f"Reason: The sum of angles is {angle_sum}°, but it must be exactly 180°.")
    if x <= 0 or y <= 0 or z <= 0:
            print("-> Reason: All angles must be greater than 0°.")


# 9.Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit

cost_price = int(input("Enter the cost: "))
selling_price = int(input("Enter the selling price: "))


profit = selling_price - cost_price
loss = cost_price - selling_price

if selling_price > cost_price:
    print(f"You got a profit of {profit}")
else:
    print(f"You got a loss of {loss}")


# # 10 Write a program that will determine weather when the value of temperature and humidity is provided by the user.
# TEMPERATURE(C)      HUMIDITY(%)      WEATHER

#       >= 30                             >=90                Hot and Humid
#       >= 30                             < 90                 Hot
#       <30                                >= 90               Cool and Humid
#       <30                                 <90                 Cool


temp = int(input("Enter the temperature: "))
humidity = int(input("Enter the humidity: "))


if temp >= 30 and humidity >= 90:
    print("Hot and Humid")
elif temp>=30 and humidity<90:
    print("Hot")
elif temp < 30 and humidity >= 90:
    print("Cool and Humid")
elif temp<30 and humidity<90:
    print("Cool")


# 11 Write a program that will take three digits from the user and add the square of each digit.

import math

x,y,z = map(int,input().split())

x = math.pow(x,2)
y = math.pow(y,2)
z = math.pow(z,2)

sum = x+y+z

print(f"Sum of square of three digit = {sum}")


# 12 Write a program that will check whether the number is armstrong(Narcissist) number or not.

number = int(input("Enter the number: "))

if number<0:
     "Negative numbers cannot be Armstrong!"

temp = number
num_digit = 0

while temp > 0:
    num_digit += 1
    temp //=1

temp = number

total_sum = 0
while temp > 0:
    digit = temp % 10
    total_sum += digit ** num_digit
    temp //= 10

print(total_sum == number)


# 13 Write a program that will give you the in hand salary after deduction of HRA(10%),DA(5%),PF(3%), and tax(if salary is between 5-10 lakh–10%),(10-20lakh–20%),(>20– 30%)(0-1lakh print k).


gross_salary = int(input("Enter your gross salaray: "))


HRA = gross_salary*0.1
DA = gross_salary*0.05
PF = gross_salary*0.03

tax = 0

if 500000<= gross_salary <=1000000:
    tax = gross_salary*0.1
elif 1000000<= gross_salary <=2000000:
    tax = gross_salary*0.2
elif gross_salary >=2000000:
    tax = gross_salary*0.3

in_hand = gross_salary - (HRA + DA + PF + tax)


if 0 <= in_hand <= 100000:
    print(f"{in_hand / 1000:.1f}k")
else:
    print(f"₹{in_hand:,.2f}")

# 14 Write a menu driven program - 1.cm to ft  2.kl to miles  3.usd to inr  4.exit

    while True:
        user_input = input("""Choose an option:
                        1.cm to ft
                        2.kl to miles
                        3.usd to inr
                        4.exit \n""")

        if user_input=="1":
            centimeter = int(input("Enter the value: "))
            feet = centimeter/30.48
            print(f"{centimeter} cm = {feet} feet")
        elif user_input == "2":
            kl = int(input("Enter the value: "))
            mile = kl*0.621371
            print(f"{kl} kilometer = {mile} miles")
        elif user_input == "3":
            usd = int(input("Enter the value: "))
            inr = usd*95.11
            print(f"{usd} USD = {inr} INR")
        elif user_input == "4":
            exit()
        else:
            print("Invalid option")


# 15 Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.

head = int(input("Enter the number of heads: "))
legs= int(input("Enter the number of legs: "))

if legs % 2 != 0 or legs < (head * 2) or legs > (head * 4):
    print("No valid solution found for the given heads and legs.")
else:
    dogs = (legs - (head * 2)) // 2
    chickens = head - dogs

    
    print(f"Dogs: {dogs}")
    print(f"Chickens: {chickens}")


# 16 Write a program to find the sum of first n numbers, where n will be provided by the user. Eg if the user provides n=10 the output should be 55


n = int(input("Enter the number: "))


sum= n(n+1)/2

print(f"Sum of 10 numbers: {sum}")