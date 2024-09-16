import math


print("print pizza")
# print("Comment")


# Variables (String, Int, float, boolean)

# String
name = "Khalifa"
job = "DevOps Engineer"

# Integer
age = 24
height = 191

# float

shoeSize = 46.5
Gpa = 3.15

# Boolean

isMarried = False
isAlive = True

print(f"{name}{job}{age}{height}{shoeSize}{Gpa}{isMarried}")


# Type Casting  str(), int(), float(), bool()

print(type(age))
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

friend = 0
friend += 2

friend -= 1
friend *= 3

friend /= 1
friend **= 2

remainder = friend % 2

print(f"{friend}, {remainder}")


x = 3.14
y = 4
z = 5

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


conditional