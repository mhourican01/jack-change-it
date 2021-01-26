from Card import Card

# Nts: consider method overloading here

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