from random import shuffle

from cards import *
from players import *

"""
The Deck class is used to perform all start-of-game operations on the deck of cards, including: 
shuffling, splitting the deck, and dealing the cards. 
Relies on the Card class for suits and ranks.
"""

user_name = input("What is your name? \n")  # global variable to store user's name


class Deck:
    def __init__(self):
        self.whole_deck = [(suit, rank) for suit in Cards.SUIT for rank in Cards.RANK]

    def shuffle_deck(self):
        print("Hello, " + user_name + "! Welcome to War!")
        print("Shuffling cards...")
        shuffle(self.whole_deck)

    def split_deck(self):
        split_deck = (self.whole_deck[:26], self.whole_deck[26:])  # splits the deck in half at the middle index
        return split_deck

    def deal_cards(self, first_half, second_half):
        print("Dealing cards...")
        user = Players(user_name, first_half)  # user is given the first half of 52
        cpu = Players("CPU", second_half)  # cpu is given the second half of 52
        print("Cards have been dealt!")
        return user, cpu

    # prepares deck to be played by shuffling, splitting, and dealing the deck to two players
    def prepare_deck(self):
        deck = Deck()
        deck.shuffle_deck()
        first_half, second_half = deck.split_deck()
        print("Press enter to deal the cards.")
        input()
        user_hand, cpu_hand = deck.deal_cards(first_half, second_half)
        print("Press enter to start playing.")
        input()
        return user_hand, cpu_hand
