import math
import time


# print("print pizza")
# print("Comment")


# Variables (String, Int, float, boolean)

# String
# name = "Khalifa"
# job = "DevOps Engineer"
#
# # Integer
# age = 24
# height = 191
#
# # float
#
# shoeSize = 46.5
# Gpa = 3.15
#
# # Boolean
#
# isMarried = False
# isAlive = True
#
# print(f"{name}{job}{age}{height}{shoeSize}{Gpa}{isMarried}")


# Type Casting  str(), int(), float(), bool()

# print(type(age))
# age = str(age)
# print(type(age))

#Accept user input()
# name = input("Hello, what is your name?: ")
# age = int(input("Hello, what is your age?: "))
# age += 1
#
# print(f"Hello {name}, Nice to meet you!")
# print(f"{age}")


# Exercise one

# Calculate the area of a rectangle

# length = float(input("What is your length? "))
# breadth = float(input("What is your breadth? "))

# Area = length * breadth

# print(f"{Area}cm²")

# Exercise Two
# MadLibs Game


# Operators

# friend = 0
# friend += 2
#
# friend -= 1
# friend *= 3
#
# friend /= 1
# friend **= 2
#
# remainder = friend % 2
#
# print(f"{friend}, {remainder}")
#
#
# x = 3.14
# y = 4
# z = 5

# result = round(x)
# result = floor(x)
# result = abs(x)
# result = pow(4, 3)
# result = min(x, y, z)
# result = max(x, y, z)
# print(f"{result}")

# x = 9.1
# result = math.floor(x)
# print(math.pi)
# print(math.e)
# print(f"{result}")
#
#
# a = float(input("enter your values for side A: "))
# b = float(input("enter your values for side B: "))
#
# # c = math.sqrt(a**2 + b**2)
# c = math.sqrt(pow(a,2) + pow(b,2))
# print(c)


# conditional statement
# age = int(input("How old are you? "))
# if age >= 18:
#     print(f"your are old enough")
# elif age < 0:
#     print(f"your are haven't been born yet")
# else:
#     print(f"your are not old enough")

#logical operator

# || = or
# && = and
# ! = not

# conditional expression || ternary operator

# access_level = "guest"
# age = 25
#
# access_level = "Full access" if access_level == "admin" else "Limited access"
# age = "Adult" if age >= 18 else "Child"
#
# print(access_level)

# String methods

# len() || length
# find()
# rfind() //last occurence, if it can't find hence results to -1
# capitalize()
# uppercase()
# lowercase()
# isdigit() when a string returns only digits and it is a boolean
# isalpha() when a string returns only strings, no spaces allowed and it is a boolean
# count() to count the number of occurence
# replace() to convert some characters with another



# username = (input("Enter your username: "))
#
# if len(username) > 12:
#     print("Your username must be less than 12 characters")
# elif " " in username:
#     print("Your username must not include a space")
# elif username.isdigit():
#     print("Your username must contain only alphabets")
# else:
#     print(f"{username} is valid")


# string indexing

# credit_cardNumber = "1223-4532-1772-1983"
#
# print(credit_cardNumber[::-1])
# the starting is inclusive but the ending is exclusive


# format specifier

# price1 = 100.23
# price2 = -87.786
# price3 = 10000.08
#
# print(f"{price1:+.2f}")
# print(f"{price2:+.1f}")
# print(f"{price3:+,.0f}")


# looping(while)

# age = int(input("Enter your age: "))
#
# while not age > 18:
#     age = int(input("Enter your age: "))
#     print(f"Your age is too small. Please try again.")

# for loop

# for x in range(1, 11, 2):
#     print(f"{x} x {x} = {x * x}")

# Set timeout
# my_time = int(input("Enter time in seconds: "))
#
# for x in range(my_time, 0 , -1):
#     seconds = int(x % 60)
#     minutes = int(x / 60) % 60
#     hour = int(x / 3600)
#
#     print(f"{hour:02}:{minutes:02}:{seconds:02}")
#
#     time.sleep(1)
#


# print rectangle

# length = int(input("Enter length: "))
# breadth = int(input("Enter breadth: "))
#
# for x in range(length):
#     print("-", end="")
# for y in range(breadth):
#      print("|")


# Collection
#List  array equivalent ordered and changeable
#Set  no duplicate value and immutable. Removing items are possible
#Tuple unchangeable and ordered.

fruits = ["apple", "orange", "cherry"]

print(fruits[1])
print(len(fruits))
print("pineapple" in fruits)

for fruit in fruits:
    print(fruit)