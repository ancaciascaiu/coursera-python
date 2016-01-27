#Exercise 4.6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate)

nrhrs = raw_input ("How many hours did you work this week? ")
rte = raw_input ("What`s the base rate? ")

def computepay(nrhrs,rte):
    try:
        hours= int(nrhrs)
        rate= int(rte)
        if hours <= 40:
            pay= hours * rate
        else:
            pay= (40*rate) + (hours-40) * (1.5*rate) 
        print pay
    except:
        print "Please enter a number!!!"
computepay(nrhrs,rte)

