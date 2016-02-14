

import urllib
from BeautifulSoup import *
accum = 0

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)


tags = soup('span')

for tag in tags:
	global accum
	nr = int(tag.contents[0])
	accum += nr
print accum