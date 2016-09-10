import random
heads = 0
tails = 0
for x in range(1,5001):
	if random.random()< .5:
		heads+=1
		print "Attempt #"+str(x)+":Throwing a coin... It's a head Got "+str(tails)+" tails so far and "+str(heads)+" heads so far"
	else:
		tails+=1
		print "Attempt #"+str(x)+":Throwing a coin... It's a tail Got "+str(tails)+" tails so far and "+str(heads)+" heads so far"
