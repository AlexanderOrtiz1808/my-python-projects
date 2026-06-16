print("Welcome to Mini Trivia!")
print("General Knowledge")
print("-" * 30)

trivia = [
    ("Question 1: What is the coldest place on Earth?", "antarctica"),
    ("Question 2: What is the longest river in the world?", "amazon"),
    ("Question 3: Where did the Olympic Games originate?", "greece"),
    ("Question 4: How many bones are in the human body?", "206"),
    ("Question 5: What is the largest country in the world?", "russia")
]

points = 0

for question, correct_answer in trivia:
    attempts = 3
    
    while attempts > 0:
        # .lower() converts everything to lowercase and .strip() removes extra spaces
        response = input(f"{question} ").lower().strip()
        
        if response == correct_answer:
            print("Correct! You have earned 10 points.\n")
            points += 10
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect answer. You have {attempts} attempts left.")
            else:
                print("You got zero points on this question. Good luck with the next one!\n")

print("-" * 30)
print(f"Congratulations! You scored {points}/50 points in total.")
print("Thank you for playing.")
