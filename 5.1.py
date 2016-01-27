
count=0
total=0

while True:
    nr=raw_input("Enter a number: ")
    if nr == "done": break
    num=int(nr)
    count=count+1
    total=total+num
print "Total: ", total, "Count: ", count, "Average: ", total/count