def scoresGrades():
	print "Scores and Grades"
	for x in range(0, 10):
		score = input('Enter Your Score')
		if (score >= 60 and score < 70):
			print ("Score: " + str(score) + "; Your grade is D")
		elif (score >= 70 and score < 80):
			print ("Score: " + str(score) + "; Your grade is C")
		elif (score >= 80 and score < 90):
			print ("Score: " + str(score) + "; Your grade is B")
		elif (score >= 90):
			print ("Score: " + str(score) + "; Your grade is B")
		else:
			print("null")

scoresGrades()

