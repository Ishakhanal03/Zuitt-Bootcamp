from abc import ABC, abstractclassmethod
class Person(ABC):
	@abstractclassmethod
	def getFullName(self):
		pass

	def addRequest(self):
		pass

	def checkRequest(self):
		pass

	def addUser(self):
		pass

class Employee(Person):
	def __init__(self, firstName, lastName, email, department):
		super().__init__()
		self._firstName = firstName
		self._lastName = lastName
		self._email = email
		self._department = department

	# getters and setter for firstname
	def getFirstName(self):
		return self._firstName

	def setFirstName(self, firstName):
		self._firstName = firstName

	# getters and setter for lastname
	def getLastName(self):
		return self._lastName

	def setLastName(self, lastName):
		self._lastName = lastName

	# getters and setter for email
	def getEmail(self):
		return self._email

	def setEmail(self, email):
		self._email = email

	# getters and setter for department
	def getDepartment(self):
		return self._department

	def setDepartment(self, department):
		self._department = department

	def getFullName(self):
		return f"{self._firstName} {self._lastName}"

	def addRequest(self):
		return "Request has been added"

	def checkRequest(self):
		return f"Checking the request"

	def addUser(self):
		return f"User has been added"

	def login(self):
		return f"{self._email} has logged in" 

	def logout(self):
		return f"{self._email} has logged out"

class TeamLead (Person):
	def __init__(self, firstName, lastName, email, department):
		super().__init__()
		self._firstName = firstName
		self._lastName = lastName
		self._email = email
		self._department = department
		self._member = []

	# getters and setter for email
	def getEmail(self):
		return self._email

	def setEmail(self, email):
		self._email = email

	# getters and setter for department
	def getDepartment(self):
		return self._department

	def setDepartment(self, department):
		self._department = department

	def getFullName(self):
		return f"{self._firstName} {self._lastName}"

	def addRequest(self):
		return "Request has been added"

	def checkRequest(self):
		return f"Checking the request"

	def addUser(self):
		return f"User has been added"

	def login(self):
		return f"{self._email} has logged in" 

	def logout(self):
		return f"{self._email} has logged out"

	def addMember(self, employee):
		self._member.append(employee)

	def get_members(self):
		return self._member


class Admin (Person):
	def __init__(self, firstName, lastName, email, department):
		super().__init__()
		self._firstName = firstName
		self._lastName = lastName
		self._email = email
		self._department = department

	# getters and setter for email
	def getEmail(self):
		return self._email

	def setEmail(self, email):
		self._email = email

	# getters and setter for department
	def getDepartment(self):
		return self._department

	def setDepartment(self, department):
		self._department = department

	def getFullName(self):
		return f"{self._firstName} {self._lastName}"

	def addRequest(self):
		return "Request has been added"

	def checkRequest(self):
		return f"Checking the request"

	def addUser(self):
		return f"User has been added"

	def login(self):
		return f"{self._email} has logged in" 

	def logout(self):
		return f"{self._email} has logged out"

	def adduser(self):
		return f"New user added"

class Request():
	def __init__(self, name, requester, dateRequested):
		self.name = name
		self.requester = requester
		self.dateRequested = dateRequested
		self.status = "Open"

	def updateRequest(self, new_request):
		self.status = new_request

	def set_status(self, new_status):
		self.status = new_status

	def closeRequest(self):
		return f"Request {self.name} has been {self.status}"

	def cancelRequest(self):
		return f"Request {self.name} has been canceled."

# Test cases:
employee1 = Employee("John", "Doe", "djohn@mail.com", "Marketing")
employee2 = Employee("Jane", "Smith", "sjane@mail.com", "Marketing")
employee3 = Employee("Robert", "Patterson", "probert@mail.com", "Sales")
employee4 = Employee("Brandon", "Smith", "sbrandon@mail.com", "Sales")
admin1 = Admin("Monika", "Justin", "jmonika@mail.com", "Marketing")
teamLead1 = TeamLead("Michael", "Specter", "smichael@mail.com", "Sales")
req1 = Request("New hire orientation", teamLead1, "27-Jul-2021")
req2 = Request("Laptop repair", employee1, "1-Jul-2021")

assert employee1.getFullName() == "John Doe", "Full name should be John Doe"
assert admin1.getFullName() == "Monika Justin", "Full name should be Monika Justin"
assert teamLead1.getFullName() == "Michael Specter", "Full name should be Michael Specter"
assert employee2.login() == "sjane@mail.com has logged in"
assert employee2.addRequest() == "Request has been added"
assert employee2.logout() == "sjane@mail.com has logged out"

teamLead1.addMember(employee3)
teamLead1.addMember(employee4)
for indiv_emp in teamLead1.get_members():
    print(indiv_emp.getFullName())

assert admin1.addUser() == "User has been added"

req2.set_status("closed")
print(req2.closeRequest())



		