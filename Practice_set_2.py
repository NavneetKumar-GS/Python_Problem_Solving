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


# 10 Write a python program to remove all the duplicates from a list


num = [1,1,2,3,4,5,5,6,5,7,7,8,2,2]

unique_num = list(set(num))
print(unique_num)


# 11. Write a python program to convert a string to title case without using the title()


string = input("Enter a string: ").lower()


words = string.split()

final_words = []

for word in words:
    cleaned_words = word[0].upper() + word[1:].lower()
    final_words.append(cleaned_words)


final_string = " ".join(final_words)
print(final_string)


# 12. Write a python program to find the max item from a list without using the max function

numbers = list(input("Enter the numbers: "))

max_value = numbers[0]

for num in numbers:
    if num>max_value:
        max_value = num

print(max_value)



# 13. Write a python program to reverse a list


num = [1,2,3,4,5,6,8]

reverse_list = num[::-1]
print(reverse_list)


# 14. Write a python program to search a given number from a list

num = int(input("Enter the number to find: "))

list = [1,2,3,4,5,6,8]

if num in list:
    print(f"{num} is in the list")
else:
    print(f"{num} is not in the list")

# 15.Write a program that can create a new list from a given list where each item in the new list is square of the item of the old list

user_input = list(input("Enter the number to form a list: "))
old_list = [int(num) for num in user_input]

new_list = [pow(num,2) for num in old_list ]

print("Original List:", old_list)
print("Squared List: ", new_list)

# 16. Write a program that can reverse words of a given string.
            # Eg if the input is Hello how are you
            # Output should be you are how Hello


string = input("Enter the string: ")

words = string.split()

reversed_string = words[::-1]

final_string = " ".join(reversed_string)


print(string)
print(final_string)


# 17.Write a program that can count the number of words in a given string

string = input("Enter the string: ")

count=0
words = string.split()
for word in enumerate(words):
    count+=1

print(f"Your string has {count} words")


# 18.Write a program to check if a list is in ascending order or not

list1 = [9,8,7,6,5,4,3,2,1]
list2 = [1,2,3,4,5,6,7,8,9]

if list1 == sorted(list2):
    print("True")
else:
    print("False")

if list1 == sorted(list2):
    print("True")
else:
    print("False")

# 19. Create 2 lists from a given list where 1st list will contain all the odd numbers from the original list and the 2nd one will contain all the even numbers 

list = [1,2,3,4,5,6,7,8,9]

even_list = []
odd_list = []

for num in list:
    if num%2==0:
        even_list.append(num)
    elif num%2!=0:
        odd_list.append(num)
    else:
        print("List is not a integer")

# 20. Write a program to merge 2 list without using the + operator

list1 = [1,2,3,4,]
list2 = [5,6,7,8,]

list1.extend(list2)

print("Merged List:", list1)


# 21.Write a program to replace an item with a different item if found in the list 

my_list = ["apple", "banana", "cherry", "banana", "date"]

old_item = "banana"
new_item = "orange"

for i in range(len(my_list)):
    if my_list[i] == old_item:
        my_list[i] = new_item
print("Updated List:", my_list)


# 22.write a program that can convert a 2D to 1D


matrix_2D = [[1,2,3],[4,5],[6,7,8,9]]
list_1d = []

for sublist in matrix_2D:
    for item in sublist:
        list_1d.append(item)

print("Original 2D List:", matrix_2D)
print("Flattened 1D List:", list_1d)

