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


# 4.Extract username from a given email. 
# Eg if the email is nitish24singh@gmail.com then the username should be nitish24singh


email = input("Enter the email: ")

username = email.split('@')[0]
print(username)


# 5.Count the frequency of a particular character in a provided string. Eg 'hello how are you' is the string, the frequency of h in this string is 2.

string = input("Enter a string: ")
char = input("Enter which char to count: ")

freq=string.count(char)
print(freq)


# 6. Find the index position of a particular character in string. 

string = input("Enter the string: ")
char = input("Enter the char to find the index: ")

pos = string.find(char)
print(pos)


# 7. Count the number of vowels in a string provided by the user.

string = input("Enter the string: ").lower()
char_to_check = ['a','e','i','o','u']

count=0

for char in char_to_check:
    if char in string:
        count += 1
print(count)


# 8. Write a program which can remove a particular character from a string. 

string = input("Enter the string: ")
char = input("Enter the char to remove: ")

final_string = string.replace(char,"")
print(final_string)


# 9. Write a program that can check whether a given string is palindrome or not.

string = input(":Enter the string: ").lower()

if string == string[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

