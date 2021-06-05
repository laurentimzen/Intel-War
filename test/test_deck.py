from deck import *


def test_number_of_cards_in_deck():
    deck_instance = Deck()
    assert 52 == len(deck_instance.whole_deck)


def test_number_of_cards_in_first_half_of_split():
    deck_instance = Deck()
    first_half, second_half = deck_instance.split_deck()
    assert 26 == len(first_half)


def test_number_of_cards_in_second_half_of_split():
    deck_instance = Deck()
    first_half, second_half = deck_instance.split_deck()
    assert 26 == len(second_half)
