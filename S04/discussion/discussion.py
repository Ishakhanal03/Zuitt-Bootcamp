# Python has several structures to store collections or multiple 
# items in a single variable: List, Dictionary, Tuples, and Set.
# For this course, we are just going to focus with list and dictionaries

# [Section] Lists
# Lists are very similar to arrays in JS in a sense that they can 
# contain a collection of data and also access its element through the index

# To create a list, the square brackets([]) is used.
names = ["Jhon", "Paul", "George", "Ringo"];
# This is an example of what we call String List.
programs = ['developer career', 'pi-shape', 'courses'];
# Example Number llist:
durations = [260, 180, 20];
# Example of Boolean List / truth tables
truth_values =[True, False, True, True, False];

#Example of a list that contains elements with different data type:
sample_list = ["Apple", 3, False, "Potato", 4, True];

print(sample_list);

# Get the size or the number of elements in our lists:
# The number of elements can be countes using the len() method;
# len(listName);

print(len(programs));

# Accessing values
	# List can be accessed by providing the index number of the element.
	# the index numbers in list starts with 0 and the last elements
	# will be len -1, where len is the number of our elements.
	# listName[indexElement];
print(names[2]);
print(durations[-1]);

# To access the last element on our array withouyt using the negative index, we can actually use the len method of our list
print(truth_values[len(truth_values) - 1]);
print(names[len(names) - 1]);

# Access a range of values
# Syntax: listName[startingIndex: endingIndex]
# Note that the ending index is not included.
# If the ending index is large or greater than length last index
# On our list it will include all the elements starting from the starting index up to the last element. 

print(names[0 : 3]);
print(names[0 : 4]);
print(sample_list[1 : 10]);

# Update element on our List 
print(names);
names[0] = "John Doe";
print(names);

# List Manipulations
# List has methods that can be used to manipulate the elements within.

# Add element to the List: append() method.
print(durations);
durations.append(301);
print(durations);

# Deleting an element from the array: del keyword.

del durations[1];
print(durations);

# Check whether element is part of the list or not.
# We want to check whether 20 is included in the durations array
print(20 in durations); #True value
print(21 in durations);

# Sort list - sort method, sorts the list alphanumerically, ascending by default.
print(names);
names.sort();
print(names);

# Clear/remove all the elements - the clear(), this is used to empty the contents of the list.
test_list = [1,3,5,7,9];
print(test_list);
test_list.clear();
print(test_list);

# [Section] Dictionaries
# Dictionaries are used to store data values in key:value pairs. This is similar with objects in other programming languages.
# Dictionary is a collection which is ordered, changeable, and doest not allow duplicates.

person1 = {
	"name" : "Brandon",
	"age" : 28,
	"occupation" : "student",
	"isEnrolled" : True,
	"subjects" : ["Python", "SQL", "Django"]
}

# To get the number of key:value pairs in the dictionary, we also use the len() method.
print(len(person1));

# Accessing values in the dictionary
# To get the items in the dictionary, the key name can be referred using the square notation
print(person1["isEnrolled"]);
print(person1["subjects"]);
print(person1["subjects"][1]);

# Get all the keys from the Dictionary - keys() method
print(person1.keys());

# Get all the values from the Dictionary - values() method
print(person1.values());

# The items() method will return each item in our dictionary, as a key-value pair in a list.
print(person1.items());

# Adding key-value pairs, it can be done with either putting a new
# index key and assigning a value or the update() method:

person2 = {
	"name" : "Chris",
	"age" : 25,
	"occupation" : "instructor",
	"isEnrolled" : False,
	"subjects" : ["Python", "SQL", "Django", "JS", "Java", "PHP"]
}

print(person2);
person2["nationality"] = "Filipino";
print(person2);

# update method

person2.update({"fave_food":"Sinigang"});
print(person2);

# Deleting entries can be done using the pop() method or the del keyword
person2.pop('fave_food');
print(person2);

del person2['nationality'];
print(person2);

# the clear() method empties the dictionary
person3 = {
	"name" : "John",
	"age" :30
}
print(person3)
person3.clear()
print(person3)

# Looping through the dictionary 
for key in person2:
	print(f"The value of {key} is {person2[key]}");

# Nested Dictionaries - dictionaries inside of a dictionary
person4 = {
	"name" : "Monika",
	"age" : 20,
	"occupation" : "poet",
	"isEnrolled" : True,
	"subjects" : ["Python" ,"SQL","Django"]
}
classRoom = {
	"student1" : person2,
	"student2" : person4
}

# [Section] Mini Exercise
# 1. Create a car dictionary with the following keys:
# brand, model, year of make, color
# 2. Print the following statement from the details:
# "I own a <Brand> <Model> and it was made in <Year of Make>"

car = {
	"brand" : "Nissan" ,
	"model" : "Altima",
	"year_of_make" : 2020,
	"color" : "Red"
}
print(f"I own a {car['brand']} {car['model']} and it was made in {car['year_of_make']}");

# Functions are blocks of code that runs when called.
# A function can be used to get inputs, process the inputs, and return outputs.
# Imagine the process of learning: inputs like lessons are processed by the brain and with the processed data, a project is the output
# The "def" keyword is used to create a function. The syntax is: 
# def <function name>():

#defines a function called my_greeting
def my_greeting():
	# code to be run when the function is called
	print('Hello User!')

# Calling/Invoking a function - specify the function name and provide values if needed
my_greeting()

# Parameters can be added to functions to have more control to what the inputs for the function will be.
def greet_user(username):
	print(f"Hello {username}!")

# Arguments are the values that are substituted to the parameters
greet_user('Hillary')
greet_user("Chris")

# Return Statements - the "return" keyword allow functions to return values

def addition(num1, num2):
	return num1 + num2 

sum = addition(5, 10)
print(f"The sum is {sum}")

# A lambda function is a small anonymous function that can be used for callbacks
# It is just like any normal python function, except that it has no name when defining it, and it is contained in one line of code.
# A lambda function can take any number of arguments, but can only have one expression.

multiply = lambda a, b : a * b
print(multiply(5,6))
print(multiply(6,99))

# Classes would serve as blueprints to describe the concept of objects
# Each object has characteristics (properties) and behaviors (objects)
# Imagine the concept of a car; a car has a brand, model, year_of_make and is able to drive, brake, turn
# To create a class, the "class" keyword is used along with the class name that starts with an uppercase character
# class ClassName():
class Car():
	# properties that all Car objects must have are defined in a method called init
	# Any number of parameters to .__init__() can be passed but the first parameter should always be self
	def __init__(self, brand, model, year_of_make):
		self.brand = brand
		self.model = model
		self.year_of_make = year_of_make

		# other properties can be added and assigned hard-coded values
		self.fuel = "Gasoline"
		self.fuel_level = 20

	#method - function inside of a class
	def fill_fuel(self):
		print(f"Current fuel level: {self.fuel_level}")
		print(f"Filling up the fuel tank....")
		self.fuel_level = 100
		print(f"New fuel level: {self.fuel_level}")

# instance of a class
new_car = Car('Nissan', 'GT-R', 2019)

print(f"My car is a {new_car.brand} {new_car.model}")

new_car.fill_fuel()


