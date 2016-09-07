def draw_stars(x):
	star = "*"
	for e in x:
		print star*e
draw_stars()

def draw_stars2(x):
	star = '*'
	for e in x:
		if type(e) is str:
			e.lower()
			print e[0]*len(e)
		if type(e) is int:
			print star*e
draw_stars2()


