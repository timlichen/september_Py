def scores():
	print 'Scores and Grades'
	for i in range(0, 10):
		score = input('Score: ')
		print 'Your grade is', ('D' if (score < 70) else ('C' if (score < 80) else ('B' if (score < 90) else 'A'))), '\n'


def longscores():
	print 'Scores and Grades'
	for i in range(0, 10):
		score = input('Score: ')
		if (score < 70):
			score = 'D'
		elif (score < 80):
			score = 'C'
		elif (score < 90):
			score = 'B'
		else:
			score = 'A'
		print 'Your grade is', score, '\n'