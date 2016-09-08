def draw_stars(a):
	for e in a:
		print e * '*' if type(e) is int else e[0].lower() * len(e)
draw_stars([1,'Scott',3,4])