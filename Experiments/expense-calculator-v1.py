initial_budget = int(input("What is your budget for today? "))

while initial_budget > 0:
    purchase = input("What did you buy? ")
    expense = int(input(f"How much did you spend on {purchase}? "))
    initial_budget -= expense
    
    response = input("Do you want to record another expense? (yes/no): ").strip().lower()
    
    if response == "yes":
        print("Okay, let's continue.")
    elif response == "no":
        print(f"Alright, your current balance is {initial_budget} pesos.")
        break

if initial_budget <= 0:
    print("You have run out of funds, bro!")
    
    
