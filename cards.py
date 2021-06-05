class Cards:
    SUIT = 'H S D C'.split()  # Heart, Spade, Diamond, Club
    RANK = 'A K Q J 10 9 8 7 6 5 4 3 2'.split()  # highest to lowest

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank