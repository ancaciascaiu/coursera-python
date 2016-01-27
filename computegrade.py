#Rewrite the grade programfrom the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string

scr= raw_input ("Please enter a score between 0.0 and 1.0: ")

def computegrade(scr):
    try:
        score = float(scr)
    
        if score>=0.9 and score <=1.0:
            print"Grade A"
        elif score >=0.8 and score <0.9:
            print "Grade B"
        elif score >=0.7 and score < 0.8:
            print "Grade C"
        elif score >=0.6 and score < 0.7:
            print "Grade D"
        elif score <0.6 and score >=0.0:
            print "Grade F"
        else:
            print "Out of range!!!"
    except:
        print " This is not a number!!!"

computegrade(scr)