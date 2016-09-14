class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def displayInfo(self):
		print "This car costs $" + str(self.price) + ", can attain a maximum velocity of " + self.max_speed + ", and has driven " + str(self.miles) + " miles."
		return self
	def ride(self):
		print "Riding"
		self.miles += 10
		return self
	def reverse(self):
		if self.miles >= 5:
			print "Reversing"
			self.miles -= 5
			return self
		else:
			return self

harley = Bike(20000, "100mph")
mitsubishi = Bike(50000, "180mph")
vespa = Bike(5000, "30mph")

harley.ride().ride().ride().ride().reverse().displayInfo().reverse().ride().reverse().displayInfo()

mitsubishi.ride()
mitsubishi.ride()
mitsubishi.reverse()
mitsubishi.reverse()
mitsubishi.displayInfo()

vespa.reverse()
vespa.reverse()
vespa.reverse()
vespa.displayInfo()