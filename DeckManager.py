from Card import Card
import random

def createDeck(suits, ranks, deck):

    # Iterating through ranks and suits
    for s in suits:
        for r in ranks:
            # Constructing card object, and adding it to deck
            if (r == 'Ace' and s == 'Hearts') or r == 2 or r == 8 or r == 'Jack' or r == 'Queen':
                c = Card(r, s, True)
            else:
                c = Card(r, s, False)

            deck.append(c)

# Assigns to each player seven cards, removing them from deck
def dealStartingHand(players, deck):

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

def updateUpcard(discardPile, upcard, c, p, isJackPlayed, suits):

    # Add upcard to discard pile
    discardPile.append(upcard)

    # Check whether Jack has been played
    if isJackPlayed:

        print("You have played a Jack! To which suit would you like to change the upcard?")
        for s in suits:
            print(str(suits.index(s) + 1) + ".", s)
        selectedSuit = input()

        upcard = Card('Jack', suits[int(selectedSuit) - 1], True)

        print("The suit has been changed to " + upcard.suit + "!")
    else:
        # Change upcard to latest card played
        upcard = c

        # Remove played card from hand
    
    p.hand.remove(c)

    return upcard