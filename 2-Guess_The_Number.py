# template for "Guess the number" mini-project  http://www.codeskulptor.org/#user40_xByRaYrDt4oH3Z0.py
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import math
import random

rang = 100
secret_number = 0
guesses_counter = 0

# helper function to start and restart the game
def new_game():
    global guesses_counter
    global rang
    global secret_number
    
    secret_number = random.randrange (0, rang)
    if rang == 100:
        guesses_counter = 7
    else:
        guesses_counter = 10
 
    print "New game: Range is 0 to ", rang, ". You have ",guesses_counter," guesses left!\n"

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global rang
    rang = 100
    global guesses_counter
    guesses_counter = 7
    print "New game: Range is 0 to 100. You have 7 guesses left!\n"

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global rang
    rang = 1000
    global guesses_counter
    guesses_counter = 10
    print "New game: Range is 0 to 1000. You have 10 guesses left!\n"
    
def input_guess(guess):
    # main game logic goes here	
    
    global guesses_counter
    num = int(guess)
    
    guesses_counter = guesses_counter - 1
    print "Guess was", num
    print "Guesses left:", guesses_counter
    
    global secret_number
    if num == secret_number:       
        print "Correct!\n"
        new_game()
    elif num > secret_number:
        print "Lower!\n"
    elif num < secret_number:
        print "Higher!\n"
        
    if guesses_counter == 0:
        print "Game over!"
        new_game()
        return
    
    
    
    
# create frame
frame = simplegui.create_frame("Guess the number!", 250, 250)

# register event handlers for control elements and start frame
button1 = frame.add_button('[0, 100)', range100, 100)
button2 = frame.add_button('[0, 1000)', range1000, 100)
inp = frame.add_input('Enter your guess', input_guess, 100)
frame.start()



# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
