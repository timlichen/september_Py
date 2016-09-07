def score_and_grades():
	for i in range(0, 10):
		grade = input("Enter your score ")
		if grade >= 90:
			print "Score: " + str(grade) + "; Your grade is A"
		elif grade >= 80:
			print "Score: " + str(grade) + "; Your grade is B"
		elif grade >= 70:
			print "Score: " + str(grade) + "; Your grade is C"
		elif grade >= 60:
			print "Score: " + str(grade) + "; Your grade is D"
		else:
			print "Please enter integer between 60 and 100"
	print "End of the program. Bye!"
score_and_grades()