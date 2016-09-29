import random
random_num = random.random();

def coinToss():
	head = 0
	tail = 0
	for x in range(1, 5001):
		if (random.random() > .5):
			tail += 1
			print "Attempt #" + str(x) + "Throwing a coin. It is tails! Got " + str(tail) + "tails. Got " + str(head) + "heads."
		else:
			head += 1
			print "Attempt #" + str(x) + "Throwing a coin. It is heads! Got " + str(tail) + "tails. Got " + str(head) + "heads."

coinToss()