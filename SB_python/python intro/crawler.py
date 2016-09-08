# import the urlopen function from the urllib2 module
from urllib2 import urlopen
# import the BeautifulSoup function from the bs4 module
from bs4 import BeautifulSoup
# import pprint to print things out in a pretty way
import pprint
# choose the url to crawl
url = 'http://www.codingdojo.com'
# get the result back with the BeautifulSoup crawler
soup = BeautifulSoup(urlopen(url))
print soup # print soup to see the result!!
# your code here to find all the links from the result
# and complete the challenges below

#CHALLENGE 1

links = soup.findAll('a')
for i in range(0, len(links)):
	soup.findAll('a')[i]['href']

#CHALLENGE 2

dictionary = {}

links = soup.findAll('a')
for i in range(0, len(links)):
	if str(soup.findAll('a')[i]['href'])[:4] == "http":
		if str(soup.findAll('a')[i]['href'])[:4] in dictionary.keys():
			dictionary[str(soup.findAll('a')[i]['href'])] += 1
		else:
			dictionary[str(soup.findAll('a')[i]['href'])] = 1