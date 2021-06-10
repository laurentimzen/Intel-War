from play_war import *

"""
In order to run these tests successfully, please use the command line. 
While within the folder "Intel-War", run the following command in order
to run the tests: 
python -m pytest -s test/test_play_war.py
When the tests load, hit the enter key to run the full tests. 
"""


def test_user_wins_with_larger_rank():
    play_instance = PlayWar()
    user_card = ('H', 'A')
    cpu_card = ('D', '5')
    assert play_instance.determine_winning_card(user_card, cpu_card) == 'user'


def test_cpu_wins_with_larger_rank():
    play_instance = PlayWar()
    user_card = ('H', '9')
    cpu_card = ('D', '10')
    assert play_instance.determine_winning_card(user_card, cpu_card) == 'cpu'


def test_equal_cards_result_in_war():
    play_instance = PlayWar()
    user_card = ('H', 'J')
    cpu_card = ('D', 'J')
    assert play_instance.determine_winning_card(user_card, cpu_card) == 'war'


def test_played_card_removed_from_hand():
    play_instance = PlayWar()
    user_cards = [('H', 'J'), ('D', 'A'), ('S', '2'), ('D', 'Q')]
    user = Players(user_name, user_cards)
    play_instance.remove_played_card_from_hand(user.hand)
    assert user.hand == [('D', 'A'), ('S', '2'), ('D', 'Q')]


def test_war_cards_removed_from_hand():
    play_instance = PlayWar()
    user_cards = [('H', 'J'), ('D', 'A'), ('S', '2'), ('D', 'Q'), ('H', 'K'), ('H', '3')]
    user = Players(user_name, user_cards)
    play_instance.remove_war_cards_from_hand(user.hand)
    assert user.hand == [('D', 'Q'), ('H', 'K'), ('H', '3')]


def test_all_cards_removed_when_not_enough_for_war():
    play_instance = PlayWar()
    user_cards = [('H', 'J'), ('D', 'A')]
    user = Players(user_name, user_cards)
    play_instance.remove_war_cards_from_hand(user.hand)
    assert user.hand == []


def test_winner_takes_both_cards():
    play_instance = PlayWar()
    cpu_card = []
    cpu = Players("CPU", cpu_card)
    winnings = [('H', '2'), ('S', '5')]
    play_instance.winner_takes_cards(winnings, cpu.hand)
    assert cpu.hand == [('H', '2'), ('S', '5')]


def test_loser_takes_no_cards():
    play_instance = PlayWar()
    user_card = []
    cpu_card = []
    user = Players(user_name, user_card)
    cpu = Players("CPU", cpu_card)
    winnings = [('H', '2'), ('S', '5')]
    play_instance.winner_takes_cards(winnings, cpu.hand)
    assert user.hand == []
