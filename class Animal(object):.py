class Animal(object):
	def __init__(self, sound, name, age, favorite_food):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_food = favorite_food
	def eat (self,favorite_food):
		print("Yummy!! " + self.name + " is eating his " + favorite_food)
	def description(self): 
		print(self.name + " is " + self.age + " years old and loves the food " + self.favorite_food)
	def make_sound(self):
		for i in range(3):
			print("The " + self.name +" "+ self.sound + "s")

animal1=Animal("roar", "lion", "9", "meat")
animal1.eat("meat")

animal1.description()

animal1.make_sound()

