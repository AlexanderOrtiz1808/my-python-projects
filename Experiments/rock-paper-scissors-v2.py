import random

choices = ("rock", "paper", "scissors")

player_points = 0
pc_points = 0

print("Welcome to Rock, Paper, Scissors! \n")
print("Remember, if you want to end the game, just type: exit \n")

while True:
    player_choice = input("Choose Rock, Paper, or Scissors: ").lower().strip()
    
    # Check for exit first to prevent the PC from getting an unfair point
    if player_choice == "exit":
        print("Thanks for playing!")
        print(f"Final Score -> You: {player_points} | PC: {pc_points}")
        break
        
    pc_choice = random.choice(choices)
    
    if player_choice == pc_choice:
        print(f"Tie! Both chose {pc_choice}. +1 point each!")
        player_points += 1
        pc_points += 1
    elif player_choice == "rock" and pc_choice == "scissors":
        player_points += 1
        print("You win! Rock smashes scissors. +1 point")
    elif player_choice == "paper" and pc_choice == "rock":
        player_points += 1
        print("You win! Paper beats rock. +1 point")
    elif player_choice == "scissors" and pc_choice == "paper":
        player_points += 1
        print("You win! Scissors cut paper. +1 point")
    else:
        print("You lose! The computer has defeated you.")
        pc_points += 1
        print(f"The computer chose: {pc_choice}")
        
