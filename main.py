from play_war import *


def main():
    play = PlayWar()
    user, cpu = deck_instance.prepare_deck()
    play.taking_turn(user, cpu)


if __name__ == "__main__":
    main()