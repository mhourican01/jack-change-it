from player import Player
from card import Card
import random

suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
deck = []
players = []

def playGame():

    global upcard
    upcard = deck[0]

    print("The upcard is: " + str(upcard.rank) + " of " + upcard.suit)

    for p in players:
        print("Player " + str(p.number) + ", it's your turn.")
        displayCards(p)

def displayCards(p):

    print("Your cards are:")
    for c in p.hand:
        print(str(c.rank) + " of " + c.suit)

    print("Which would you like to play?")

    playableCards = {}
    
    for c in p.hand:
        if (c.rank == upcard.rank or c.suit == upcard.suit):

            print(str(c.rank) + " of " + c.suit)

def initialiseGame():

    createDeck()
    initialisePlayers()
    dealCards()
    playGame()

def createDeck():

    for s in suits:
        for r in ranks:
            
            c = Card(s, r)
            deck.append(c)

def initialisePlayers():

    noOfPlayers = input("How many players are there? ")

    for n in range(1, (int(noOfPlayers) + 1)):
        p = Player(n, None)
        players.append(p)

def dealCards():

    random.shuffle(deck)
    startingHand = 7
    
    for p in players:

        hand = []

        for count in range(0, startingHand):

            hand.append(deck[count])
            deck.remove(deck[count])
        
        p.hand = hand

initialiseGame()