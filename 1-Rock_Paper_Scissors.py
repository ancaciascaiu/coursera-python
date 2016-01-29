# Rock-paper-scissors-lizard-Spock template http://www.codeskulptor.org/#user40_oZjFgixy4J6JC6f.py

def name_to_number(name):
    if name=="rock":
        number = 0
    elif name=="Spock":
        number = 1
    elif name=="paper":
        number = 2
    elif name=="lizard":
        number = 3
    elif name=="scissors":
        number = 4
    else:
        return None
    return number

def number_to_name(number):
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        return None
    return name
    

def rpsls(player_choice): 
   
    print " "

    print "Player chooses", player_choice
    player_number = name_to_number(player_choice)
    
    import random
    comp_number = random.randrange(5)
    comp_choice= number_to_name(comp_number)
    print "Computer chooses", comp_choice

    mod = (comp_number - player_number) % 5 
    if mod == 1 or mod == 2:
        print "Player wins!"
    elif mod == 3 or mod == 4:
        print "Computer wins!"
    else: 
        print "Player and computer tie!" 
    
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

