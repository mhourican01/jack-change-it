from Card import Card

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

# If player has no playable cards, draw one
def drawCard(p, deck):
    print("You have no playable cards! Draw a card.")
    p.hand.append(deck[0])
    deck.pop(0)

# If player plays Two, next player draws two cards
def drawTwoCards(p, deck):

    """
    if players.index(p) == len(players) - 1:
        nextPlayer = players[0]
    else:
        nextPlayer = players[players.index(p) + 1]

    hasTwo = False
    for c in nextPlayer.hand:
        if c.rank == 2:
            hasTwo = True
            break

    if not hasTwo:
        """

    print("Player " + str(p.number) + ", a Two was played! You must draw two cards.")

    for n in range(0, 2):
            p.hand.append(deck[0])
            deck.pop(0)

# If Ace of Hearts was played, player draws five cards
def drawFiveCards(p, players, deck):

    print("Player " + str(p.number) + ", the Ace of Hearts was played! You must draw five cards.")

    for n in range(0, 5):
        p.hand.append(deck[0])
        deck.pop(0)