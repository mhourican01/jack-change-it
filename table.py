from player import Player
from card import Card
import random

suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
deck = []
players = []

def main():

    createDeck()
    initialisePlayers()
    dealCards()
    
    global upcard
    # Setting upcard to first card in deck
    upcard = deck[0]

    print("The upcard is: " + str(upcard.rank) + " of " + upcard.suit)

    # Controlling turns
    for p in players:

        print("Player " + str(p.number) + ", it's your turn.")
        displayCards(p)

# Creates card objects, and adds them to deck
def createDeck():

    # Iterating through ranks and suits
    for s in suits:
        for r in ranks:
            
            # Constructing card object, and adding it to deck
            c = Card(s, r)
            deck.append(c)

# Asks user to input number of players, and creates as many player objects
def initialisePlayers():

    noOfPlayers = input("How many players are there? ")

    # Creating player objects until user input, number of players, is reached
    # Player hand set to null until cards are dealt
    for n in range(1, (int(noOfPlayers) + 1)):
        p = Player(n, None)
        players.append(p)

# Assigns to each player seven cards, removing them from deck
def dealCards():

    random.shuffle(deck)
    startingHand = 7
    
    for p in players:

        # Temporary hand to populate
        hand = []

        # Looping until starting hand of seven cards is reached
        for count in range(0, startingHand):

            #Adding card to hand, and removing from deck
            hand.append(deck[count])
            deck.remove(deck[count])
        # Setting player's hand to temporary hand
        p.hand = hand

# Displays active player's hand, and playable cards
def displayCards(p):

    # Temporary list to store playable cards
    playableCards = []

    print("Your cards are:")

    for c in p.hand:

        print(str(c.rank) + " of " + c.suit)

        # If a card matches the upcard in rank or suit, it is a playable card
        if (c.rank == upcard.rank or c.suit == upcard.suit):
            
            playableCards.append(c)

    print("You can play:")

    # Displaying playable cards beside number for selection
    for c in playableCards:

        print(str(playableCards.index(c) + 1) + ".", str(c.rank) + " of " + c.suit)

    # Asking user to select card
    noOfPlayers = input("Which would you like to play? ")

    for c in playableCards:

        if (noOfPlayers == playableCards.index(c) + 1):
            
            # upcard = c
            p.hand.remove(c)

    print("Player " + str(p.number) + ", you have " + str(len(p.hand)) + " cards remaining.")
    print("The new upcard is " + str(upcard.rank) + " of " + upcard.suit)

main()