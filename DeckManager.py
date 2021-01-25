from Card import Card

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