def updateUpcard(discardPile, upcard, c, p):

    # Add upcard to discard pile
    discardPile.append(upcard)
    
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
def drawTwoCards(p, players, deck):

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

        print("You have played a Two! Player " + str(nextPlayer.number) + " must draw two cards.")

        nextPlayer.hand.append(deck[0])
        nextPlayer.hand.append(deck[1])

        deck.pop(0)
        deck.pop(1)