#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.



name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

accumulator=dict()

for line in handle:
    words = line.split()
    if len(words) < 2 : continue
    if words[0] != "From" : continue
    second = words[1]
    
    accumulator[second] = accumulator.get(second,0) + 1
 
   
maxVal = None
maxKey = None
 
for name,key in accumulator.items():
    if maxKey  is None or key > maxVal:
        maxKey  = name
        maxVal = key
       
print maxKey, maxVal
 