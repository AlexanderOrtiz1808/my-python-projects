import random

salaries = []
for i in range(100):
    generated_salary = random.randint(10000, 50000)
    salaries.append(generated_salary)
    
print("Welcome to the mini data analyzer \n")

while True:
    print("What would you like to do now?")
    print("1. View maximum salary")
    print("2. View minimum salary")
    print("3. Calculate average")
    print("4. Exit \n")
    
    user_choice = input("What would you like to do? ").strip().lower()
    
    if user_choice == "1":
        print(f"The maximum salary is: {max(salaries)}")
    elif user_choice == "2":
        print(f"The minimum salary is: {min(salaries)}")
    elif user_choice == "3":
        print(f"The average salary is: {sum(salaries)/len(salaries)}")
    else:
        print("You have exited the mini data analyzer")
        break
    