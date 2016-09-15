class Car(object):
	def __init__(self, price, speed, fuel, mileage, tax):
		self.price = price
		self.speed = price
		self.fuel = fuel
		self.mileage = mileage
		if self.price > 10000:
			self.tax = .15
		else:
			self.tax = .12

	def display_all(self):
		car_info = str(self.price) + self.speed + self.fuel + self.mileage + str(self.tax)

civic = Car(20000, "95mph", "Full", "15mpg")
civic.display_all()
