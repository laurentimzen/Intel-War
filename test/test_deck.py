from deck import *

"""
In order to run these tests successfully, please use the command line. 
While within the folder "Intel-War", run the following command in order
to run the tests: 
python -m pytest -s test/test_deck.py
When the tests load, hit the enter key to run the full tests. 
"""


def test_number_of_cards_in_deck():
    deck_instance = Deck()
    assert 52 == len(deck_instance.whole_deck)


def test_shuffling_changes_order():
    deck_instance = Deck()
    assert deck_instance.shuffle_deck() != deck_instance.whole_deck


def test_number_of_cards_in_first_half_of_split():
    deck_instance = Deck()
    first_half, second_half = deck_instance.split_deck()
    assert 26 == len(first_half)


def test_number_of_cards_in_second_half_of_split():
    deck_instance = Deck()
    first_half, second_half = deck_instance.split_deck()
    assert 26 == len(second_half)


def test_split_decks_are_different():
    deck_instance = Deck()
    first_half, second_half = deck_instance.split_deck()
    assert first_half != second_half


def test_dealt_hands_are_equal_size():
    deck_instance = Deck()
    first_half, second_half = deck_instance.split_deck()
    user, cpu = deck_instance.deal_cards(first_half, second_half)
    assert len(user.hand) == len(cpu.hand)


def test_dealt_hands_are_different():
    deck_instance = Deck()
    first_half, second_half = deck_instance.split_deck()
    user, cpu = deck_instance.deal_cards(first_half, second_half)
    assert user.hand != cpu.hand


