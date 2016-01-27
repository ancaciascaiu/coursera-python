#10.2 Write a program to read through the mbox-short.txt and figure out 
#the distribution by hour of the day for each of the messages. You can 
#pull the hour out from the 'From ' line by finding the time and then 
#splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, 
#sorted by hour as shown below. Note that the autograder does not have support 
#for the sorted() function.


name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)


accum=[]

for line in handle:
    words = line.split()
    if len(words) < 2 : continue
    if words[0] != "From" : continue
    sixth = words[5]
    hour_min=sixth.split(':')
    hour=hour_min[0]
    
    accum.append(hour)
    accum.sort()
    
distrib={} 
for hr in accum:
    distrib[hr]=distrib.get(hr,0)+1

l=list()
for key, val in distrib.items():
    l.append((key,val))
    
    print key, val

 
