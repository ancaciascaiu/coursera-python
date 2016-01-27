import random

m = []
x = []
star = True

for i in range(10):
    m.append(random.randint(0,10))
    
print m


#while m:
for j in range(len(m)-1):
    
    for m[j] in m:
        if m[j]< m[j+1]:
            x.append(m[j+1])
            x.append(m[j])

        else:
            pass
        #            x.append(m[j])
        #            x.append(m[j+1])
print x
