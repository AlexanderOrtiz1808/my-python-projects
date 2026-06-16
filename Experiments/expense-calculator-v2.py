print("Welcome to your expense calculator. \n")
initial_budget = int(input("What is your budget for today? "))

while initial_budget > 0:
    purchase = input("What will you buy? ")
    expense = int(input("How much will you spend on that? "))
    
    if expense > initial_budget:
        print("Insufficient funds! You cannot buy that.\n")
    else:
        initial_budget -= expense
        print(f"Expense recorded. You have {initial_budget} pesos left.\n")
        
    response = input("Do you want to record another expense? ").strip().lower()
    
    if response == "yes":
        print("Okay, let's continue.\n")
    elif response == "no":
        print(f"Alright, your current balance is {initial_budget} pesos.\n")
        break

if initial_budget == 0:
    print("You have run out of funds, bro\n")

