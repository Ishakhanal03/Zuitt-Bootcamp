# Python allows for user inputs, with this, users can give inputs to the program

# [Section] input() method -  allows our users to give or to add input to our program.

# Example:
username = input("Please enter your name:\n");
print(f"Hello {username} ! Welcome to the Python Course!");

# type() method checks what is the data type of the varaible
print(type(username));

# The default data type of the value from the input method is String.

# If you want to convert the data type of the inputted value into integer or int you have to use the int() method.
# It will convert the string into data type

num1 = int(input("Enter 1st number:\n"));
num2 = int(input("Enter 2nd number:\n"));
print(f"The sum of the num1 and num2 is {num1 + num2}");

# [Section] With the user inputs, users can give inputs for the program to be used to control the application using control structures
	# Selection Control Structure  - allows the program to choose among choices and run specific codes depending on the choice taken.
	# Repitition Control Structures - allows the program to repeat certain blocks of code given a starting condition and terminating condition.

# Selection Control Structure (If - Else Statement):
# If-else statements are used to choose between two or more code blocks depending on the condition

test_num = 75;

if test_num >= 75:
	print("Test Passed!");
	print("Test is actually pass!");
else:
	print("Test Failed!");

# We are now going to use the if statement on the user input

test_num2 = int(input("Please enter your test number: \n"));

if test_num2 > 0 :
	print("The number is positive.");
elif test_num2 == 0:
	print("The number is neutral.");
elif test_num2 < 0 :
	print("The number is negative.");

# Repition Control Structure
# Loop 
# Python has loops that can repeat blocks of code

# WHILE Loop - are used to execute a set of statements as long as the condition is true:
i = 1;

while i<=5:
	print(f"Current Count {i}!");
	# incrementation
	i += 1;

# For loops are used for iterating over a sequence 
# We usually use for loops in lists or tuples will be discussed in the upcoming sessions

fruits = ["apple", "banana", "cherry", "mango"];

for indiv_fruit in fruits:
	print(indiv_fruit);

# range method in for loop
# to use for loop to iterate through values, the range method can be used.

for x in range (6):
	print(f"The current value of x is {x}!");
# The range method by default it starts with 0 and it will stop before the declare value.

for x in range(6, 10):
	print(f"The current values is {x}!");
# If we have two arguments on our range method, the first argument will be the starting value and the second argument will be the stopping, and the increment will still be 1.

for y in range (6 , 20 , 2):
	print(f"The current value of y is {y}!");

