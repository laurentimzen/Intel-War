# Intel-War
This is an implementation of the card game War, as requested for an interview with Intel.

# Assumptions
**This implementation makes assumptions about the conditions for winning a game of War:**

* A user has all 52 cards in their hand 
* A War occurs, and one's opponent does not have the necessary number of cards to complete the War. In this case, the person with more cards wins. 
* If the game continues for 5000 rounds, the game ends in a draw. 
    * At this point, it is assumed the game is unwinnable for either player due to the ordering of the cards. 

\
**The implementation makes assumptions about how a "War" functions:**

* A War ends when a player's "face-up" card is greater than their opponent's. The person with the larger rank wins the War. 
* If a War results in two cards of equal rank, another War begins. Four more cards are played until either player has the higher rank. This may repeat multiple times until the War is won. 
* As previously stated, if one of the players does not have the necessary number of cards to complete 
the War, the player with the larger hand wins the game and takes all cards.

\
**This implementation makes assumptions about the order of a player's hand of cards:** 

* The card at the "top" of the deck is placed at the front of the list used within the program. The card at the "top" is the card that will be played next.
* When a player wins a round, the "winnings" are placed at the "bottom" of the deck, which is the back of the list used within the program. 

\
**This implementation makes assumptions about the nature of playing the game:** 

* A semi-interactive game was assumed. The beginning of the game is interactive. In order to
keep the time it takes to play the game to a minimum, the rest of the game is run automatically.
    * I experimented with letting the user play round by round by hitting "enter" at the end of each round. 
    However, as this game often takes hundreds of turns, I found this a time-consuming approach.
* This implementation assumes a command-line version of the game, using print statements. 


# Running the Program
The recommended method of running this program is via the command line. In order to run the game simulation please enter the following command while in the folder "Intel-War": 

`python main.py`

In order to give the user a somewhat immersive experience with this game, the beginning of the game 
asks the user to input their name using the keyboard. 

The user is also prompted to hit the enter key twice, once per prompt.

Once the game begins, it is run automatically. This game often takes hundreds, sometimes even thousands,
of turns to complete. In order to keep the user from having to press a key this many times, 
I believe it was most straight-forward to let the game play out in full. 

The end of the game informs the player of the winner, how many rounds the game lasted, and how many Wars occurred. 


# Running the Tests

The recommended method of running the tests for this program is via the command line. Descriptions for how to run each of the two test files are included in a comment on each file. 

To run the file `test_deck.py` please run the following command from the folder "Intel-War": 

`python -m pytest -s test/test_deck.py`

To run the file `test_play_war.py` please run the following command from the folder "Intel-War": 

`python -m pytest -s test/test_play_war.py`

For both tests, please hit the enter key after the command is run to bypass the user_name input.

# If Given More Time

* If given more time, I would have loved to develop a more visual user interface. Seeing actual cards, 
rather than representations of cards *( example: ('S', '2') represents the 2 of Spades )* would have likely
been a better, and more immersive experience for the user. 

    Although I personally enjoy the simplicity of a game played on the command line, I think War is the 
type of game that would benefit from these sorts of visual cues. 



* If given more time, I also would have liked to implement a two-player option. Rather than just play
with the CPU, as the user does in my implementation, the option to play with a second user would have
been nice. In my opinion, this feature would work best with a visual UI, as stated above. 


* This code was written as cleanly as possible, to the best of my ability given the time constraints.
Tests were written and frequently ran as I worked, comments were written, most functions were kept relatively short,
functions were given descriptive titles, and variables were named 
for clarity of purpose.

    * *( example: the list that stored the cards given to the winner at the end 
of a round was called `winnings`, which exemplifies the purpose of the variable.)*.

    However, if given more time, I think there are a couple of functions featured in this 
    implementation that could have been shortened. There are a couple instances of 
    redundant code that could have been made into their own separate functions to be called
    in place of using the same code several times.
