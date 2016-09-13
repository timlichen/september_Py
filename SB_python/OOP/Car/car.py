class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		if price > 10000:
			self.price = price + (price * .15)
		else:
			self.price = price + (price * .12)
		self.speed = speed 
		self.fuel = fuel
		self.mileage = mileage
		self.display_all()
	def display_all(self):
		print self.price, str(self.speed) + "mph", self.fuel, str(self.mileage) + "mpg"

bmw = Car(10000, 50, 12, 100000)
mercedes = Car(2000, 35, "Full", 15)
honda = Car(4314, 32, "Empty", 31)
suzuki = Car(9809009, 2, "Half", 4224)
bike = Car(23132, 312, "none", 123)
driver = Car(0, 0, "All", 0)