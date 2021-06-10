from deck import *

"""
The PlayWar class includes all the functions that are needed to play a game of War. 
The PlayWar class relies on the deck of cards created in the Deck class. 
"""

deck_instance = Deck()


class PlayWar:
    # determines winning card by comparing the rank of two cards
    # returns a string that includes who won, or if there should be a war
    def determine_winning_card(self, user_card, cpu_card):
        if user_card[1] == cpu_card[1]:
            return "war"
        elif Cards.RANK.index(user_card[1]) > Cards.RANK.index(cpu_card[1]):
            return "user"
        elif Cards.RANK.index(user_card[1]) < Cards.RANK.index(cpu_card[1]):
            return "cpu"

    # pops card from the front of the hand (the "top" of the deck)
    def remove_played_card_from_hand(self, hand):
        return hand.pop(0)

    # pops cards from the front of the hand (the "top" of the deck) when a war occurs
    # If a hand does not have enough cards (four cards) to engage in the war scenario,
    # all of the remaining cards in the deck are popped
    def remove_war_cards_from_hand(self, hand):
        war_cards = []
        if len(hand) < 4:  # there are not enough cards in the hand to go to war
            for count in range(len(hand)):
                war_cards.append(hand.pop(0))
            return war_cards
        else:
            for count in range(3):
                war_cards.append(hand.pop(0))
            return war_cards

    # adds the won cards to the back of the hand (the "bottom" of the deck)
    def winner_takes_cards(self, winnings, hand):
        hand.extend(winnings)