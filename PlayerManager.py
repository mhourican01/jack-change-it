from Player import Player

# Asks user to input number of players, and creates as many player objects
def initialisePlayers(players):

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

# Displays active player's hand, and determines playable cards
def displayHand(p, upcard):

    # Temporary list to store playable cards
    playableCards = []

    print("Your cards are:")

    for c in p.hand:

        print(str(c.rank) + " of " + c.suit)

        # If a card matches the upcard in rank or suit, it is a playable card
        if (c.rank == upcard.rank or c.suit == upcard.suit):
            
            playableCards.append(c)

    return playableCards