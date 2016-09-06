import random
def coins():
	heads = 0
	tails = 0
	for i in range(0, 5000):
		coin = ("head" if (random.random() > .5) else "tail")
		heads += 1 if coin == "head" else 0
		tails += 1 if coin == "tail" else 0
		print "Attempt #" + str(i + 1) + ": Throwing a coin... it's a " + coin + "! ... Got", heads, "head(s) so far and", tails, "tail(s) so far"
	print "Ending the program, thank you!"
coins()