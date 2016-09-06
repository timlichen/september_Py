import re

def get_matching_words(regex):
 words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

 return [word for word in words if re.search(regex, word)]

print get_matching_words('v')
print get_matching_words('ss')
print get_matching_words('e$')
print get_matching_words('b\wb')
print get_matching_words('b\w+b')
print get_matching_words('b\w*b')
print get_matching_words('a\w*e\w*i\w*o\w*u')
print get_matching_words('^[aegilnoprsux]+$')
print get_matching_words('aa|bb|cc|dd|ee|ff|gg|hh|ii|jj|kk|ll|mm|nn|oo|pp|qq|rr|ss|tt|uu|vv|ww|xx|yy|zz')