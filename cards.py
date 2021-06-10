"""
 The Card class is used to store all possible suits and ranks
 for a standard 52-card deck of cards.
"""


class Cards:
    SUIT = 'H S D C'.split()  # Heart, Spade, Diamond, Club
    RANK = '2 3 4 5 6 7 8 9 10 J Q K A'.split()  # lowest to highest

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
