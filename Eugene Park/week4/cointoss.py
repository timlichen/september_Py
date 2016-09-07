import random
def cointoss():
	head_count = 0
	tail_count = 0
	for i in range(1, 5001):
		if round(random.random()) == 0:
			head_count += 1
			print "Attempt #" + str(i) + ": Throwing a coin... It's a head! ... Got " + str(head_count) + " head(s) so far and " + str(tail_count) + " tail(s) so far"
		else:
			tail_count += 1
			print "Attempt #" + str(i) + ": Throwing a coin... It's a tail! ... Got " + str(head_count) + " head(s) so far and " + str(tail_count) + " tail(s) so far"
cointoss()