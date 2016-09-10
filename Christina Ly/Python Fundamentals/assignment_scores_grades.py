def grade(score):
	if score >=90:
		print "Score: ",score,"; Your grade is A"
	elif score>=80:
		print "Score: ",score,"; Your grade is B"
	elif score>=70:
		print "Score: ",score,"; Your grade is C"
	elif score>=60:
		print "Score: ",score,"; Your grade is D"
for test in range(1,11):
	print "Enter a score between 60 and 100"
	score = raw_input()
	if int(score) < 60 or int(score) > 100:
		print "Invalid value"
		break
	grade(int(score))
print "End of the program. Bye!"
