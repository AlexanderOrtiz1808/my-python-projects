import random

choices = ("rock", "paper", "scissors")
player_choice = input("Choose Rock, Paper, or Scissors: ").lower().strip()
pc_choice = random.choice(choices)

if player_choice == pc_choice:
    print(f"Tie! Both chose {pc_choice}!")
elif player_choice == "rock" and pc_choice == "scissors":
    print("You win! Rock smashes scissors.")
elif player_choice == "paper" and pc_choice == "rock":
    print("You win! Paper beats rock.")
elif player_choice == "scissors" and pc_choice == "paper":
    print("You win! Scissors cut paper.")
else:
    print("You lose! The computer has defeated you.")
    print(f"The computer chose: {pc_choice}")
    