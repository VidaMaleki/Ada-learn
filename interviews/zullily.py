# Let's play a game of Blackjack. We will be using rules of Blackjack that are
# simplified from the full casino rules.
#
# During the game, players start with two cards and can "hit" to ask for another
# card until they decide to stop. But you don't need to worry about that. We'll
# just be scoring the hands after they finish the game.
#
# Cards can have a numerical value between 2 and 10, or be a "face" card named
# J, Q, K, or A. All cards will be represented as strings, including number cards.
# Number cards are worth their numerical value. J, Q, and K are worth 10. A is
# worth either 1 or 11, whichever gives the player the best chance to win.
#
# Any player who gets a total of 21 with only two cards automatically wins,
# unless of course the other player also does the same, in which case it's a tie.
#
# If a player has a total of 22 or more, they automatically lose, again, unless
# the other player does the same, in which case it's a tie.
#
# Otherwise, whichever player has the higher total wins, and if they have the
# same total, it's a tie.
#
# Please write a function to determine who wins the game. It should return -1 if
# player 1 wins the game, 1 if player 2 wins the game, and 0 if it's a tie.
import random

cards = {"two","three", "four", "five", "six", "seven", "eight", "nine","ten", "A", "J", "Q", "K"}

cards_value = {"two":2,"three":3, "four":4, "five":5, "six":6, "seven": 7, "eight":8, "nine":9,"ten":10, "A":11, "J":10, "Q":10, "K":10}
def random_cards(cards):
    shuffle_cards=random.shuffle(cards)
    return shuffle_cards.pop()

def blackjack_winner(player_1_hand, player_2_hand):
    total_1 = 0
    for card in player_1_hand:
        if card == "A":
            if 21 - total <= 11:
                total_1 += 11
            else:
                total_1 += 1





def tie(a_total, b_total):
    if a_total == b_total:
        return 0

a = shuffle_cards.pop()