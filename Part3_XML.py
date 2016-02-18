import urllib
import xml.etree.ElementTree as ET




address = 'http://python-data.dr-chuck.net/comments_239517.xml'


    
print 'Retrieving', address
uh = urllib.urlopen(address)
data = uh.read()
#print 'Retrieved',len(data)
   
suma=0
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
for item in lst:
    items = item.find("count").text
    numbers = int(items)
    suma += numbers
print suma
		
    