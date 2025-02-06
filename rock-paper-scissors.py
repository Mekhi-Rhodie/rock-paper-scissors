import random
import os 

Score_File = "score.txt"

choices = ["Rock", "Paper", "Scissors"]

def load_score():
    if not os.path.exists(Score_File):
        return {"Wins": 0, "Losses": 0, "Ties": 0}
    with open(Score_File, "r") as file:
        try:
            return eval(file.read())
        except:
            return {"Wins": 0, "Losses": 0, "Ties": 0}

def save_score(score):
    with open(Score_File, "w") as file:
        file.write(str(score))

def determine_winner(player, ai):
    if player == ai:
        return "Tie"
    elif (player == "Rock" and ai == "Scissors") or \
         (player == "Scissors" and ai == "Paper") or \
         (player == "Paper" and ai == "Rock"):
        return "Win"
    else:
        return "Lose"
    
def start_game():

    score = load_score()

    print("\n Welcome to Rock, Paper, Scissors!")
    print("Type 'exit' to quit. \n")

    while True:

        player_choice = input("Enter Rock, Paper, Scissors: ").strip().lower()

        if player_choice == "exit":
            print("\nFinal Score - Wins: {}, Losses: {}, Ties: {}".format(
                score["Wins"], score["Losses"], score["Ties"]
            ))
            print("Thanks for playing! 🎉")
            break

        if player_choice not in choices:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
            continue