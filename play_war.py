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

    # includes all functionality for when a war occurs
    def go_to_war(self, winnings, user_hand, cpu_hand):
        play_instance = PlayWar()
        print("The values of the cards are equal!\nTime for War!")
        print("You will play 3 cards face-down, and 1 card face-up.")

        # if the user or the CPU do not have enough cards for war, the larger hand wins the game
        # and takes all the remaining cards in their opponent's hand
        if len(user_hand) < 4 or len(cpu_hand) < 4:
            if len(user_hand) > len(cpu_hand):
                winnings.extend(play_instance.remove_war_cards_from_hand(user_hand))
                winnings.extend(play_instance.remove_war_cards_from_hand(cpu_hand))
                play_instance.winner_takes_cards(winnings, user_hand)
                print("The CPU does not have enough cards for a War!\nYou have more cards, so you win the game!")
            else:
                winnings.extend(play_instance.remove_war_cards_from_hand(user_hand))
                winnings.extend(play_instance.remove_war_cards_from_hand(cpu_hand))
                play_instance.winner_takes_cards(winnings, user_hand)
                print("You do not have enough cards for a War!\nCPU has more cards, so you lose the game...")

        else:
            winnings.extend(play_instance.remove_war_cards_from_hand(user_hand))
            winnings.extend(play_instance.remove_war_cards_from_hand(cpu_hand))

            user_card = play_instance.remove_played_card_from_hand(user_hand)
            cpu_card = play_instance.remove_played_card_from_hand(cpu_hand)

            winnings.append(user_card)
            winnings.append(cpu_card)

            print("Your War card: ", end="")
            print(user_card)
            print("CPU's War card: ", end="")
            print(cpu_card)
            print("")

            winner = play_instance.determine_winning_card(user_card, cpu_card)
            # determines who takes the cards, or if another war should occur
            if winner == 'user':
                play_instance.winner_takes_cards(winnings, user_hand)
                print("Your card scored higher. You won the round!")
            if winner == 'cpu':
                print("The CPU card scored higher. You lost the round...")
                play_instance.winner_takes_cards(winnings, cpu_hand)
            if winner == 'war':
                play_instance.go_to_war(winnings, user_hand, cpu_hand)

    # goes through the average turns for the players
    def taking_turn(self, user, cpu):
        rounds = 0  # keeps track of total rounds of the game
        war_rounds = 0  # keeps track of how many wars occur throughout the game

        while len(user.hand) != 0 and len(cpu.hand) != 0:
            rounds += 1
            winnings = []  # declares an empty list to store the winnings each turn
            play_instance = PlayWar()

            user_card = play_instance.remove_played_card_from_hand(user.hand)
            cpu_card = play_instance.remove_played_card_from_hand(cpu.hand)

            # appends the played cards to the winnings list
            winnings.append(user_card)
            winnings.append(cpu_card)

            print("\n\n----------------------------------------------\n")
            print("Your card: ", end="")
            print(user_card)
            print("CPU's card: ", end="")
            print(cpu_card)
            print("")

            winner = play_instance.determine_winning_card(user_card, cpu_card)
            # determines what course of action to take based on who won the round
            if winner == "user":
                play_instance.winner_takes_cards(winnings, user.hand)
                print("Your card scored higher. You won the round!")
            elif winner == "cpu":
                print("The CPU card scored higher. You lost the round...")
                play_instance.winner_takes_cards(winnings, cpu.hand)
            elif winner == "war":
                war_rounds += 1
                play_instance.go_to_war(winnings, user.hand, cpu.hand)

            print("\nYou have: " + str(len(user.hand)) + " cards")
            print("CPU has: " + str(len(cpu.hand)) + " cards\n")

            # if the game continues for 5000 rounds, the game ends and is called as a draw.
            if rounds == 5000:
                print("This game of War has gone on for 5000 rounds! It is unlikely to be won. It's a draw!")
                print("\n\n----------------------------------------------\n")
                exit()

        # if either player has all 52 cards, the game ends.
        if len(user.hand) == 52:
            print("Congratulations! You won this game of War!")
        else:
            print("The CPU has all the cards! You lose this game of War...")

        print("\nThis game took " + str(rounds) + " to complete.")
        print(str(war_rounds) + " Wars took place during this game.")
        print("\n\n----------------------------------------------\n")