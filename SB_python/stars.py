def draw_stars(a):
	for e in a:
		print (e * '*' if type(e) == int else e.lower()[0] * len(e))
draw_stars([1,'Scott',3,4])