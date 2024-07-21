from abc import ABC, abstractclassmethod

class Animal(ABC):
	@abstractclassmethod
	def eat(self, food):
		pass

	@abstractclassmethod
	def make_sound(self):
		pass

class Dog(Animal):
	def __init__(self, Name, Breed, Age):
		super().__init__()
		self.Name = Name
		self.Breed = Breed
		self.Age = Age
	
	# Getters & Setters 
	def eat(self, food):
		self._food = food
		print(f'Eaten {self._food}');

	def make_sound(self):
		print(f"Bark! Woof! Arf!");

	def call(self):
		print(f"Here {self.Name}!");


class Cat(Animal):
	def __init__(self, Name, Breed, Age):
		super().__init__()
		self.Name = Name
		self.Breed = Breed
		self.Age = Age

	# Getters & Setters 
	def eat(self, food):
		self._food = food # Setter
		print(f'Serve me {self._food}'); # Getter

	def make_sound(self):
		print(f"Miaow! Nyaw! Nyaaaaa!");

	def call(self):
		print(f"{self.Name}, come on!");

# Test Cases:
dog1 = Dog("Isis", "Dalmatian", 15)
dog1.eat("Steak")
dog1.make_sound()
dog1.call()

cat1 = Cat("Puss", "Persian", 4)
cat1.eat("Tuna")
cat1.make_sound()
cat1.call()
