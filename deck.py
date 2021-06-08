from random import shuffle

from cards import *
from players import *

"""
The Deck class is used to perform all start-of-game operations on the deck of cards, including: 
shuffling, splitting the deck, and dealing the cards. 
Relies on the Card class for suits and ranks.
"""

# user_name = input("What is your name? \n")  # global variable to store user's name
user_name = "Test"  # temporary user_name variable being left for testing purposes


class Deck:
    def __init__(self):
        self.whole_deck = [(suit, rank) for suit in Cards.SUIT for rank in Cards.RANK]

    def shuffle_deck(self):
        print("Hello, " + user_name + "! Welcome to War!")
        print("Shuffling cards...")
        shuffle(self.whole_deck)

    def split_deck(self):
        split_deck = (self.whole_deck[:26], self.whole_deck[26:])  # splits the deck in half at the middle index
        # print(split_deck)
        return split_deck

    def deal_cards(self, first_half, second_half):
        print("Dealing cards...")
        user = Players(user_name, first_half)
        cpu = Players("CPU", second_half)
        print("Cards have been dealt!")
        # print(user.__dict__)
        # print(cpu.__dict__)
        return user, cpu

    def prepare_deck(self):
        deck = Deck()
        deck.shuffle_deck()
        first_half, second_half = deck.split_deck()
        user_hand, cpu_hand = deck.deal_cards(first_half, second_half)
        return user_hand, cpu_hand

        # return getattr(player_hands[0], "hand"), getattr(player_hands[1], "hand")
        # print(player_hands)
        # return player_hands

# d = Deck()
# d.prepare_deck()
# # print(d.whole_deck)
# d.shuffle_deck()
# half1, half2 = d.split_deck()
# result = d.deal_cards(half1, half2)
# print(result)
# print(result[0])
# print(getattr(result[0], "hand")[0])  # get hand from user
# # print(half1)
# print(half2)
# d.deal_cards(half1, half2)
# print(d.prepare_game())
# print(getattr())
