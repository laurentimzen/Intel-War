from random import shuffle

from cards import *


class Deck:
    def __init__(self):
        self.whole_deck = [(suit, rank) for suit in Cards.SUIT for rank in Cards.RANK]

    def shuffle(self):
        print("Shuffling cards...")
        shuffle(self.whole_deck)

    def split_deck(self):
        print("Splitting deck in half...")
        split_deck = (self.whole_deck[:26], self.whole_deck[26:])  # splits the deck in half at the middle index
        # print(split_deck)
        return split_deck

# d = Deck()
# half1, half2 = d.split_deck()
# print(half1)