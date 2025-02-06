import random
import os 

choices = ["Rock", "Paper", "Scissors"]

def determine_winner(player, ai):
    if player == ai:
        return "Tie"
    elif (player == "Rock" and ai == "Scissors") or \
         (player == "Scissors" and ai == "Paper") or \
         (player == "Paper" and ai == "Rock"):
        return "Win"
    else:
        return "Lose"