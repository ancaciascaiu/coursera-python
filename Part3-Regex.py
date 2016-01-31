#In this assignment you will read through and parse a file with text and numbers. 
#You will extract all the numbers in the file and compute the sum of the numbers.
#Sample data: http://python-data.dr-chuck.net/regex_sum_42.txt (There are 116 values with a sum=597873)


import re
import math
hand = open('regex_sum.txt')
numlist = list()
for line in hand:
	line = line.rstrip()
	x = re.findall('([0-9]+)', line)
	for number in x:
		num = float(number)
		numlist.append(num)

#-------------------------------------------#	
			
print numlist
print "Sum:", sum(numlist)