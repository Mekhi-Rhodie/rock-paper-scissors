import random
import os 

score_File = "score.txt"

choices = ["Rock", "Paper", "Scissors"]

def load_score():
    if not os.path.exists(score_File):
        return {"Wins": 0, "Losses": 0, "Ties": 0}
    with open(score_File, "r") as file:
        try:
            return eval(file.read())
        except:
            return {"Wins": 0, "Losses": 0, "Ties": 0}

def save_score(score):
    with open(score_File, "w") as file:
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

        player_choice = input("Please choose either Rock, Paper, or Scissors: ").strip().lower()

        if player_choice == "exit":
            print("\nFinal Score - Wins: {}, Losses: {}, Ties: {}".format(
                score["Wins"], score["Losses"], score["Ties"]
            ))
            print("Thanks for playing! 🎉")
            break

        if player_choice not in choices:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
            continue

        ai_choice = random.choice(choices)
        print(f"🤖 AI chose: {ai_choice}")

        result = determine_winner(player_choice, ai_choice)

        if result == "Win":
            print("🎉 The computer wins!")
            score["Wins"] += 1
        elif result == "lose":
            print("😢 You lose!")
            score["Losses"] += 1
        else:
            print("🤝 It's a tie!")
            score["Ties"] += 1

        save_score(score)

        print(f"Score -> Wins: {score['Wins']} | Losses: {score['Losses']} | Ties: {score['Ties']}\n")

if __name__ == "__main__":
    start_game()