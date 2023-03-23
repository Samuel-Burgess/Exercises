"""Rock Paper Crossblades game"""

import easygui, random

play = "Yes"

easygui.msgbox("Welcome to Rock, Paper, Crossblades!!!!")
while play == "Yes":
    player_choice = easygui.buttonbox("What do you want to pick?", "Make your choice"
                                                                   "", choices=["Rock", "Paper", "Crossblades"])
    choices = ["Rock", "Paper", "Crossblades"]
    computer_choice = random.choice(choices)
    if player_choice == "Rock":
        if computer_choice == player_choice:
            result = "Tied"
        elif computer_choice == "Crossblades":
            result = "Win"
        else:
            result = "Loss"
    if player_choice == "Paper":
        if computer_choice == player_choice:
            result = "Tied"
        elif computer_choice == "Rock":
            result = "Win"
        else:
            result = "Loss"
    if player_choice == "Crossblades":
        if computer_choice == player_choice:
            result = "Tied"
        elif computer_choice == "Paper":
            result = "Win"
        else:
            result = "Loss"
    easygui.msgbox(f"You {result}!, the computer chose {computer_choice}, and you chose {player_choice}!", "Result")
    play = easygui.buttonbox("Do you want to play again?", "Play again", choices=["Yes", "No"])
easygui.msgbox("Thank you for playing!")
