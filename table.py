from player import Player
from card import Card
import random

suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = [8, 8, 'Queen', 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
deck = []
players = []
discardPile =[]

def main():

    createDeck()
    initialisePlayers()
    dealCards()
    
    global upcard
    # Setting upcard to first card in deck
    upcard = deck[0]

    discardPile.append(upcard)
    deck.pop(deck.index(upcard))

    print("There are " + str(len(deck)) + " cards left in the deck.")
    print("The upcard is " + str(upcard.rank) + " of " + upcard.suit + ".")

    # Inelegant
    global firstTurn
    firstTurn = True

    # Very inelegant
    global isEightPlayed
    isEightPlayed = False

    # Controlling turns
    playTurn(upcard, firstTurn, isEightPlayed)

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
    print()
    
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

def playTurn(upcard, firstTurn, isEightPlayed):

    # Controlling turns
    for p in range(len(players)):

        if firstTurn:
            activePlayer = players[0]
        elif isEightPlayed:

            skippedPlayer = players[players.index(activePlayer) + 1]
            print("Player " + str(skippedPlayer.number) + ", skip a turn!")
            if players.index(activePlayer) == len(players) - 2:
                activePlayer = players[0]
            elif players.index(activePlayer) == len(players) - 1:
                activePlayer = players[1]
            else:
                activePlayer = players[players.index(activePlayer) + 2]
        else:
            activePlayer = players[players.index(activePlayer) + 1]

        isEightPlayed = False

        print("Player " + str(activePlayer.number) + ", it's your turn.")
        print()
        playableCards = displayCards(activePlayer)

        if not playableCards:

            print()
            print("You have no playable cards! Draw a card.")

            activePlayer.hand.append(deck[0])

            deck.pop(0) 
        else:

            print()
            print("You can play:")

            # Displaying playable cards beside number for selection
            for c in playableCards:

                print(str(playableCards.index(c) + 1) + ".", str(c.rank) + " of " + c.suit)

            # Asking user to select card
            print()
            selectedCard = input("What would you like to do? ")

            for c in playableCards:

                if int(selectedCard) == (playableCards.index(c) + 1):
                    # Check that selected card is not player's last
                    if len(activePlayer.hand) > 1:
                        # Special card behaviours
                        if c.rank == 2:
                            drawTwoCards(activePlayer)
                        if c.rank == 8:
                            isEightPlayed = True
                        if c.rank == 'Queen' and len(players) >= 3:

                            players.reverse()
                            print("Players reversed!")
                        upcard = updateUpcard(upcard, activePlayer, c)
                    else:
                        print("You have played all your cards. You are the winner!")
        print("Player " + str(activePlayer.number) + ", you have " + str(len(activePlayer.hand)) + " cards left.")
        print()

        if len(deck) == 1:
            print("There is " + str(len(deck)) + " card left in the deck.")
        else:
            print("There are " + str(len(deck)) + " cards left in the deck. Discard pile: " + str(len(discardPile)))

        print("The upcard is " + str(upcard.rank) + " of " + upcard.suit + ".")
        print()

        firstTurn = False

        if players.index(activePlayer) == len(players) - 1 and (activePlayer.number == 1 or activePlayer.number == len(players)):

            firstTurn = True
            playTurn(upcard, firstTurn, isEightPlayed)

def drawTwoCards(p):

    if p.number == len(players):
        nextPlayer = players[0]
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

def updateUpcard(upcard, p, c):

    # Add upcard to discard pile
    discardPile.append(upcard)
    
    # Change upcard to most latest card played
    upcard = c

    # Remove played card from hand
    p.hand.remove(c)

    return upcard

main()