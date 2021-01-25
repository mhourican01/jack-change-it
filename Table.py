from Player import Player
from Card import Card
from CardManager import *
from DeckManager import *
import random

suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
deck = []
players = []
discardPile =[]

def main():

    createDeck(suits, ranks, deck)
    initialisePlayers()
    dealCards()
    
    global upcard
    # Setting upcard to first card in deck
    upcard = deck[0]

    discardPile.append(upcard)
    deck.pop(deck.index(upcard))

    print("There are " + str(len(deck)) + " cards left in the deck.")
    print("The upcard is " + str(upcard.rank) + " of " + upcard.suit + ".")

    # Controlling turns
    playTurn(upcard)

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

def playTurn(upcard):

    gameWon = False
    isFirstTurn = True
    isTrickPlayed = False

    # Controlling turns
    while not gameWon:
        
        if isFirstTurn:

            activePlayer = players[0]
            isFirstTurn = False
        else:
            activePlayer = players[players.index(activePlayer) + 1]

        #if isTwoPlayed:
        #   drawTwoCards(activePlayer, players, deck)

        if isTrickPlayed:
            if upcard.rank == 2:
                drawTwoCards(activePlayer, players, deck)
            elif upcard.rank == 8:
                print("Player " + str(activePlayer.number) + ", skip a turn!")
                if players.index(activePlayer) == len(players) - 1:
                    activePlayer = players[0]
                else:
                    activePlayer = players[players.index(activePlayer) + 1]

        isTrickPlayed = False

        print("Player " + str(activePlayer.number) + ", it's your turn.")
        print()

        playableCards = displayCards(activePlayer)

        if not playableCards:

            drawCard(activePlayer, deck)
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
                        # Trick card behaviours
                        if c.isTrick == True:
                            isTrickPlayed = True

                        if c.rank == 'Queen' and len(players) >= 3:

                            players.reverse()
                            print("Players reversed!")

                        upcard = updateUpcard(discardPile, upcard, c, activePlayer)
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

        if players.index(activePlayer) == len(players) - 1:
            isFirstTurn = True
main()