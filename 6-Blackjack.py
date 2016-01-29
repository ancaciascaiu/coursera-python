# Mini-project #6 - Blackjack   http://www.codeskulptor.org/#user40_q7mslwADNaK7nqN.py

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
current = ""
dealer = []
player = []
deck = []


# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank, down):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank
        self.faceDown = down
        
    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        if self.faceDown == False:
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        else:
            card_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])
            canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_SIZE)
          
        
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []	# create Hand object

    def __str__(self):
        return ','.join([card.get_suit()+card.get_rank() for card in self.hand])# return a string representation of a hand

    def add_card(self, card):
        self.hand.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        sum = 0
        ace = False
        for card in self.hand:
            sum += VALUES.get(card.get_rank())
            if card.get_rank() == 'A':
                ace = True
        if ace and sum <= 10:
            return sum+10
        else:
            return sum
    
    def hit(self, deck):
        self.add_card(deck.deal_card())

    def busted(self):
        global busted
        sum = self.get_value()
        if sum > 21:
            return True	# compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        for card in self.hand:
            card.draw(canvas, [50+80*self.hand.index(card), pos[1]])	# draw a hand on the canvas, use the draw method for cards
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for s in SUITS:
            for r in RANKS:
                self.deck.append(Card(s, r, False))
        self.shuffle()	# create a Deck object

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)    # use random.shuffle()

    def deal_card(self):
        return self.deck.pop()	# deal a card object from the deck
    
    def __str__(self):
        pass	# return a string representing the deck



#define event handlers for buttons
def deal():
    global outcome, current, in_play, dealer, player, deck, score
    if in_play:
        score -= 1
    deck = Deck()
    dealer = Hand()
    player = Hand()
    outcome = ""
    current = "Hit or Stand?"
    in_play = True
    dealer.hit(deck)
    player.hit(deck)
    dealer.hit(deck)
    player.hit(deck)

def hit():
    global in_play, outcome, score, current
    if in_play == True:
        player.hit(deck)	# replace with your code below
        if player.busted():
            outcome = 'You went bust!'
            current = 'New deal?'
            in_play = False
    # if the hand is in play, hit the player
            score -= 1
        if player.get_value() == 21:
            in_play = False
            outcome = 'You got BLACKJACK!'
            current = 'New deal?'
            score += 1
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global outcome, in_play, score, current
    if in_play == True:	
        while dealer.get_value() < 17:
            dealer.hit(deck)
            if dealer.busted():
                outcome = "Dealer went bust!"
                score += 1
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
        if not dealer.busted() and dealer.get_value() > player.get_value():
            outcome = "Dealer won."
    # assign a message to outcome, update in_play and score
            score -= 1
        if not dealer.busted() and dealer.get_value() == player.get_value():
            outcome = "It's a tie."
        if not dealer.busted() and dealer.get_value() < player.get_value():
            outcome = "You won."
            score += 1
    in_play = False
    current = "New deal?"
    
def draw(canvas):
    global in_play
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Score: "+str(score), (400, 100), 26, "Black")
    canvas.draw_text("Blackjack", (70,100), 38, "Blue")
    canvas.draw_text("Dealer", (70, 180), 26, "Black")
    canvas.draw_text(outcome, (220, 180), 26, "Black")
    canvas.draw_text("Player", (70, 530), 26, "Black")
    canvas.draw_text(current, (320, 380), 26, "Black")
    dealer.draw(canvas, [300, 300])
    player.draw(canvas, [300, 400])
    card = Card("S", "A", in_play)
    card.draw(canvas, [50,200])
            

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric