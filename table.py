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

    print("There are " + str(len(deck)) + " cards left in the deck.")
    print("The upcard is " + str(upcard.rank) + " of " + upcard.suit + ".")

    # Controlling turns
    playTurn(upcard)

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
    
    try:
        if int(noOfPlayers) < 2:
            print("That's too few players! Please enter a number between 2-6.")
            initialisePlayers()
        elif int(noOfPlayers) > 6:
            print("That's too many players! Please enter a number between 2-6.")
            initialisePlayers()
        else:
            # Creating player objects until user input, number of players, is reached
            # Player hand set to null until cards are dealt
            for n in range(1, (int(noOfPlayers) + 1)):
                p = Player(n, None)
                players.append(p)
    except ValueError:
        print("That's not a number! Please enter a number between 2-6.")
        initialisePlayers()

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

    return playableCards

def playTurn(upcard):

    # Controlling turns
    for p in players:

        print("Player " + str(p.number) + ", it's your turn.")
        playableCards = displayCards(p)

        if not playableCards:

            print("You have no playable cards! Draw a card.")

            p.hand.append(deck[0])

            deck.pop(0)
            
        else:
            print("You can play:")

            # Displaying playable cards beside number for selection
            for c in playableCards:

                print(str(playableCards.index(c) + 1) + ".", str(c.rank) + " of " + c.suit)

            # Asking user to select card
            selectedCard = input("What would you like to do? ")

            for c in playableCards:

                if int(selectedCard) == (playableCards.index(c) + 1):
                    
                    if c.rank == 2:
                        drawTwoCards(p)

                    if c.rank == 8:
                        
                        upcard = c
                        break

                    if len(p.hand) > 1:
                        # Change upcard to card user played
                        upcard = c

                        # Remove played card from hand
                        p.hand.remove(c)
                    else:
                        print("You have played all your cards. You are the winner!")

        print("Player " + str(p.number) + ", you have " + str(len(p.hand)) + " cards left.")
        if len(deck) == 1:
            print("There is " + str(len(deck)) + " card left in the deck.")
        else:
            print("There are " + str(len(deck)) + " cards left in the deck.")
        print("The upcard is " + str(upcard.rank) + " of " + upcard.suit + ".")

        if upcard.rank == 8:
            continue

        if p.number == len(players):
            playTurn(upcard)

def drawTwoCards(p):

    if p.number == len(players):
        nextPlayer = players.index(0)
    else:
        nextPlayer = players[players.index(p) + 1]

    hasTwo = False

    for c in nextPlayer.hand:

        if c.rank == 2:

            hasTwo = True
            break

    if not hasTwo:

        print("You have played a Two! Player " + str(nextPlayer.number) + " must draw two cards.")

        nextPlayer.hand.append(deck[0])
        nextPlayer.hand.append(deck[1])

        deck.pop(0)
        deck.pop(1)

#def skipTurn():

main()