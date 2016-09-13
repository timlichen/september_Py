class Animal(object):
	def __init__(self, name, health):
		self.name = name
		self.health = health
	def walk(self):
		self.health -= 1
		return self
	def run(self):
		self.health -= 5
		return self
	def displayHealth(self):
		print self.health
		return self

animal = Animal('Scott', 100)
animal.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
	def __init__(self, name):
		super(Animal, self).__init__()
		self.health = 150
	def pet(self):
		self.health += 5
		return self

dog = Dog("no")
dog.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
	def __init__(self, name):
		super(Animal, self).__init__()
		self.health = 170
	def fly(self):
		self.health -= 10
		return self
	def displayHealth(self):
		print "This is a dragon!"
		super(Dragon, self).displayHealth()

dragon = Dragon("yes")
dragon.walk().walk().walk().run().run().fly().fly().displayHealth()