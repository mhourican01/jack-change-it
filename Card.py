# Constructor for card objects, possessing a rank and suit
class Card:

  def __init__(self, rank, suit, isTrick):

    self.rank = rank
    self.suit = suit
    self.isTrick = isTrick
