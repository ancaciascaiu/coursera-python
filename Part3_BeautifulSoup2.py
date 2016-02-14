import urllib
from BeautifulSoup import *
the_full_list=[]
url = 'http://python-data.dr-chuck.net/known_by_Connolly.html '  #raw_input('Enter - ')
i=0
while i<8:
	print "Retrieving " + str(url) 
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	tags = soup('a')	
	url = tags[17]["href"]
	i += 1
   
    
    
	
	
    
	
    

    
	

