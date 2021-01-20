from player import Player
from card import Card
import random

suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
deck = []
players = []
upcard = None

def playGame():

    upcard = deck[0]

    print("The upcard is: " + str(upcard.rank) + " of " + upcard.suit)

    for p in players:
        print("Player " + str(p.number) + ", it's your turn.")
        displayCards(p)

def displayCards(p):


    playableCards = []

    print("Your cards are:")

    for c in p.hand:

        print(str(c.rank) + " of " + c.suit)

        if (c.rank == upcard.rank or c.suit == upcard.suit):
            
            playableCards.append(c)

    print("You can play:")

    for c in playableCards:

        print(str(playableCards.index(c) + 1) + ".", str(c.rank) + " of " + c.suit)

    noOfPlayers = input("Which would you like to play? ")

    for c in playableCards:
        if (noOfPlayers == playableCards.index(c) + 1):
            
            
            upcard = c
            p.hand.remove(c)

    print("Player " + str(p.number) + ", you have " + str(len(p.hand)) + " cards remaining.")
    print("The new upcard is " + str(upcard.rank) + " of " + upcard.suit)

def initialiseGame():

    createDeck()
    initialisePlayers()
    dealCards()
    playGame()

# Creates card objects and adds them to deck list
def createDeck():

    for s in suits:
        for r in ranks:
            
            c = Card(s, r)
            deck.append(c)

# Asks user to input number of players, and creates as many player objects
def initialisePlayers():

    noOfPlayers = input("How many players are there? ")

    for n in range(1, (int(noOfPlayers) + 1)):
        p = Player(n, None)
        players.append(p)

# Assigns to each player seven cards, removing them from deck
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