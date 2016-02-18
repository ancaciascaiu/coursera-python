import json
import urllib

input = 'http://python-data.dr-chuck.net/comments_239521.json'

uh = urllib.urlopen(input)
data = uh.read()
info = json.loads(data)

#print info["comments"]["name"]
print 'User count:', len(info)
rmation = info["comments"]
#print rmation


suma = 0
for item in rmation:
    nr=item["count"]
    numbers = int(nr)
    suma += numbers
    
print suma