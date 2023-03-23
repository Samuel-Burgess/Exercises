"""Yahtzee! lite v2"""

import random
import easygui


def roll_dice():
    return [random.randint(1, 6) for _ in range(5)]


def count_dice(dice):
    count = [0] * 7
    for d in dice:
        count[d] += 1
    return count


def print_dice(dice):
    easygui.msgbox("You rolled: " + " ".join(str(d) for d in dice))


def play_yahtzee():
    easygui.msgbox("Welcome to Yahtzee!")
    scores = [0, 0]
    for player in range(2):
        easygui.msgbox(f"Player {player + 1}, it's your turn!")
        rolls_left = 3
        dice = roll_dice()
        print_dice(dice)
        while rolls_left > 0:
            action = easygui.buttonbox("Do you want to Stick or Roll again?", choices=["Stick", "Roll"])
            if action == "Stick":
                count = count_dice(dice)
                if 5 in count[1:]:
                    easygui.msgbox("Yahtzee!")
                    scores[player] = 50
                    break
                elif 4 in count[1:]:
                    easygui.msgbox("Four of a kind!")
                    scores[player] = sum(dice)
                    break
                elif 3 in count[1:]:
                    easygui.msgbox("Three of a kind!")
                    scores[player] = sum(dice)
                    break
                else:
                    easygui.msgbox("Better luck next time")
                    break
            elif action == "Roll":
                rolls_left -= 1
                dice = roll_dice()
                print_dice(dice)
        if rolls_left == 0:
            count = count_dice(dice)
            if 5 in count[1:]:
                easygui.msgbox("Yahtzee!")
                scores[player] = 50
            elif 4 in count[1:]:
                easygui.msgbox("Four of a kind!")
                scores[player] = sum(dice)
            elif 3 in count[1:]:
                easygui.msgbox("Three of a kind!")
                scores[player] = sum(dice)
            else:
                easygui.msgbox("Better luck next time")
    easygui.msgbox(f"Player 1's score: {scores[0]}\nPlayer 2's score: {scores[1]}")
    if scores[0] > scores[1]:
        easygui.msgbox("Player 1 wins!")
    elif scores[1] > scores[0]:
        easygui.msgbox("Player 2 wins!")
    else:
        easygui.msgbox("It's a tie!")


play_yahtzee()

