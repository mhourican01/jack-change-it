from Player import Player
from Card import Card
from CardManager import *
from DeckManager import *
from PlayerManager import *

suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
deck = []
players = []
discardPile =[]

def main():

    createDeck(suits, ranks, deck)
    initialisePlayers(players)
    dealStartingHand(players, deck)

    global upcard
    # Setting upcard to first card in deck
    upcard = deck[0]

    discardPile.append(upcard)
    deck.pop(deck.index(upcard))

    print("There are " + str(len(deck)) + " cards left in the deck.")
    print("The upcard is " + str(upcard.rank) + " of " + upcard.suit + ".")

    # Controlling turns
    playTurn(upcard, deck)

# Nts: Consider making below func main

def playTurn(upcard, deck):

    gameWon = False
    isFirstTurn = True
    isTrickPlayed = False

    # Controlling turns
    while not gameWon:

        isJackPlayed = False
        
        if isFirstTurn:

            activePlayer = players[0]
            isFirstTurn = False
        else:
            activePlayer = players[players.index(activePlayer) + 1]

        if isTrickPlayed:
            if upcard.rank == 'Ace' and upcard.suit == 'Hearts':
                drawFiveCards(activePlayer, players, deck)
            if upcard.rank == 2:
                drawTwoCards(activePlayer, deck)
            elif upcard.rank == 8:
                print("Player " + str(activePlayer.number) + ", skip a turn!")
                if players.index(activePlayer) == len(players) - 1:
                    activePlayer = players[0]
                else:
                    activePlayer = players[players.index(activePlayer) + 1]

        isTrickPlayed = False

        print("Player " + str(activePlayer.number) + ", it's your turn.")
        print()

        playableCards = displayHand(activePlayer, upcard)

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
                        
                            if c.rank == 'Jack':
                                isJackPlayed = True
                                upcard = updateUpcard(discardPile, upcard, c, activePlayer, isJackPlayed, suits) 
                            elif c.rank == 'Queen' and len(players) >= 3:
                                players.reverse()
                                print("Players reversed!")
                                
                        if not isJackPlayed:
                            upcard = updateUpcard(discardPile, upcard, c, activePlayer, isJackPlayed, suits)
                    else:
                        print()
                        print("You have played all your cards. You are the winner!")

        print("Player " + str(activePlayer.number) + ", you have " + str(len(activePlayer.hand)) + " cards left.")
        print()

        if len(deck) == 0:
            print("The deck is empty! The discard pile is the new deck.")
            deck = discardPile.copy()
            discardPile.clear()

        if len(deck) == 1:
            print("There is " + str(len(deck)) + " card left in the deck.")
        else:
            print("There are " + str(len(deck)) + " cards left in the deck.")

        print("The upcard is " + str(upcard.rank) + " of " + upcard.suit + ".")
        print()

        if players.index(activePlayer) == len(players) - 1:
            isFirstTurn = True
main()