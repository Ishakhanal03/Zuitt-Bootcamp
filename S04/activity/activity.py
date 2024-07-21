class Camper():
	def __init__(self, name, batch, course_type):
		self.name = name
		self.batch = batch
		self.course_type = course_type

	def career_track(self):
		print(f"Currently enrolled in the {self.course_type} program.");

	def info(self):
		print(f"My name is {self.name} of batch {self.batch}.");

zuit_camper = Camper('Kaveri Shrestha', 2077, 'Python,Django course');

print(f"Camper Name: {zuit_camper.name}");
print(f"Camper Batch: {zuit_camper.batch}");	
print(f"Camper Course: {zuit_camper.course_type}");	

zuit_camper.info();
zuit_camper.career_track();
