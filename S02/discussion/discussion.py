# [Sections] Comment
# Comments in Python are done using "#" symbol
# Reminder that comments are not read by the program and only by the user

# [Section] Python Syntax
# Hello World in pyhton
print("Hello World!!!")
print("Hello BEC003")
# Where in other programming languages the 
# indentation in code is for readbility only, 
# the indentation in Python is very important.
# In Python, indentation is used to indicate a block of code.
# Similar to JS or javascript, there is no need to 
# add delimeters or semicolons on the end of our statement or code.

# [Section] Variables 
# Variables serves as the container of our data,
# this is where we save data from our application
# In python, a variable name and assigning a value 
# using the equal symbol

# [Section] Naming Convention
# All identifiers should begin with a letter (A to Z or a to z,underscore).
# Snake casing
# Example:
age_of_the_student = 16
_age = 17
# $name = "Kaveri" - not allowed

# Example of declaring a variable:
age = 35

Age = 36

# Python allows assigning of values to multiple 
# variables in one line:
name_one, name_two, name_three, name_four = "Jhon", "Paul", "George", "Ringo"

# [Section] Data Types
# Data types convey what kind of information
# /data a varible hold. In Python, there are 
# different data types and each has its own use.

# 1. Strings(str) - for alphanumeric and symbols
full_name = "Jhon Doe"
secret_code = "Password"
another_example = "365"

# 2. Numbers(int, float, complex) for integers, 
# decimals and complex numbers
num_of_days = 365 #this is integer
pi_approx = 3.1416 #this is a decimal
complex_number = 1+5j #this is complex number because j is an imaginary component

# 3.Boolean(bool) - for truth values
is_learning = True
is_difficult = False

# [Section] Using Variables
print("My name is " + full_name)

# f-string
print(f"My name is {full_name} and my age is {age}!")

# print("My age is" + age) -> not allowed cause concatenation can only be used to print string variable

# [Section] Operations
# Python has operator families that can be use to manipulate variables

# Arithmetic Operations
# Addition
print(1 + 10)

# Subtraction
print(100-10)

# Multiplication
print(18 * 10)

# Division
print(21/3)

# Modulo 
print(18%4)

# Exponent
print(2 ** 6)

# Comparison operator
print(1 == 1)
print(1 >= 6)

# !=, >=, <=, > , <