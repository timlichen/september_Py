class MathDojo(object):
	def __init__(self):
		self.value = 0
	def add(self, *restOfArg):
		if len(restOfArg) == 1:
				self.value += restOfArg[0]
				return self
		else:
			for i in range(0, len(restOfArg)):
				print self.value
				if type(restOfArg[i]) == list or type(restOfArg[i]) == tuple:
					for x in range(0, len(restOfArg[i])):
						self.value += restOfArg[i][x]
				else:
					self.value += restOfArg[i]
			return self
	def subtract(self, *restOfArg):
		if len(restOfArg) == 1:
			self.value -= restOfArg[0]
			return self
		else:
			for i in range(0, len(restOfArg)):
				print self.value
				if type(restOfArg[i]) == list or type(restOfArg[i]) == tuple:
					for x in range(0, len(restOfArg[i])):
						self.value -= restOfArg[i][x]
				else:
					self.value -= restOfArg[i]
			return self

md = MathDojo()
print md.add([1],3,4).add([3, 5, 7, 8], (2, 4.3, 1.25)).subtract(2, [2,3], [1.1, 2.3]).value