# 1 Write a program that keeps on accepting a number from the user until the user enters Zero. Display the sum and average of all the numbers.

total = 0
count = 0


while True:
    n = int(input("Enter a number(o to stop): "))

    if n==0:
        break
    total +=n
    count+=1

print("Sum= ", total)
if count > 0:
    print("Average =", total / count)
else:
    print("No numbers were entered.")


# 2 Write a program that accepts 2 numbers from the user a numerator and a denominator and then simplifies it
#   Eg if the num = 5, den = 15 the answer should be ⅓
#   Eg if the num = 6, den = 9 the answer should be ⅔

from fractions import Fraction

num,den = int(input("Enter the denominator & numerator: "))

simplify = Fraction(numerator=num,denominator=den)

print(f"Simplification= {simplify}")


# 3. Find the length of a given string without using the len() function. 

string = input("Enter a string: ")

count = 0

for s in string:
    count= count + 1

print("Length of string =", count)
