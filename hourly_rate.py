nrhrs = raw_input ("How many hours did you work this week?")
try:
    hours= int(nrhrs)
    rate= 10

    if hours <= 40:
        pay= hours * rate
    else:
        pay= (40*rate) + (hours-40) * (1.5*rate) 
    print pay
except:
    print "Please enter a number!!!"

