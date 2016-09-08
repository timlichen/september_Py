import re

def get_matching_words(regex):
	words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]
	return [word for word in words if re.search(regex, word)]

#1
print get_matching_words('v')
#2
print get_matching_words('ss')
#3
print get_matching_words('\w*e$')
#4
print get_matching_words('b.b')
#5
print get_matching_words('b.\w*b')
#6
print get_matching_words('b.*b')
#7
print get_matching_words('.*a.*e.*i.*o.*u.*')
#8
print get_matching_words('(?<!\S)[regular expression]+(?!\S)')
#9
print get_matching_words('(\w*(\w)\\2\w*)')