"""
The Players class establishes what a Player will look like.
The game War includes two players.
The first player will be the user, and the second player will be the CPU.
Both players will have a name and a hand of cards.
"""


class Players:
    def __init__(self, player_name, hand):
        self.player_name = player_name  # includes the name of the player (user and cpu)
        self.hand = hand
