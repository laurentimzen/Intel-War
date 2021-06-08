from deck import *


class PlayWar:
    deck_instance = Deck()
    user, cpu = deck_instance.prepare_deck()
    print(user.hand)

    # deck.shuffle_deck()
    # first_half, second_half = deck.split_deck()
    # player_hands = deck.deal_cards(first_half, second_half)

    # for cards in

