class Bike(object):
	def __init__(self, price, max_speed, miles):
		self.price = price
		self.max_speed = max_speed
		self.miles = miles

	def displayInfo(self):
		print self.price
		print self.max_speed
		print self.miles

	def ride(self):
		print "riding"
		self.miles += 10
		print self.miles

	def reverse(self):
		print "reversing"
		if self.miles > 10:
		self.miles -= 10
		print self.miles

stromer = Bike(599, "50 mph", 0)
roadmaster = Bike(80, "25 mph", 0)
schwinn = Bike(300, "40 mph", 0)

stromer.ride()
stromer.ride()
stromer.ride()
stromer.reverse()
stromer.displayInfo()
roadmaster.ride()
roadmaster.ride()
roadmaster.reverse()
roadmaster.reverse()
roadmaster.displayInfo()
schwinn.reverse()
schwinn.reverse()
schwinn.reverse()
schwinn.displayInfo()




