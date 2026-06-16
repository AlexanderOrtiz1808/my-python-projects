print("Welcome to Mini Trivia!")
print("General Knowledge\n")

attempts_q1 = 3
attempts_q2 = 3
attempts_q3 = 3
attempts_q4 = 3
attempts_q5 = 3

points = 0
key = 0

# Question 1
while attempts_q1 > 0:
    response = input("Question 1: What is the coldest place on Earth? ")
    if response == "Antarctica":
        print("Correct! You have earned 10 points.\n")
        points += 10
        key += 1
        break
    else:
        attempts_q1 -= 1
        print(f"Incorrect answer. You have {attempts_q1} attempts left.\n")

if attempts_q1 == 0:
    print("You got zero points on this question. Good luck with the next ones!\n")
    key += 1

# Question 2
if key == 1:
    while attempts_q2 > 0:
        response2 = input("Question 2: What is the longest river in the world? ")
        if response2 == "Amazon":
            print("Correct! You have earned 10 points.\n")
            points += 10
            key += 1
            break
        else:
            attempts_q2 -= 1
            print(f"Incorrect answer. You have {attempts_q2} attempts left.\n")

    if attempts_q2 == 0:
        print("You got zero points on this question. Good luck with the next ones!\n")
        key += 1

# Question 3
if key == 2:
    while attempts_q3 > 0:
        response3 = input("Question 3: Where did the Olympic Games originate? ")
        if response3 == "Greece":
            print("Correct! You have earned 10 points.\n")
            points += 10
            key += 1
            break
        else:
            attempts_q3 -= 1
            print(f"Incorrect answer. You have {attempts_q3} attempts left.\n")

    if attempts_q3 == 0:
        print("You got zero points on this question. Good luck with the next ones!\n")
        key += 1
        
# Question 4
if key == 3:
    while attempts_q4 > 0:
        response4 = input("Question 4: How many bones are in the human body? ")
        if response4 == "206":
            print("Correct! You have earned 10 points.\n")
            points += 10
            key += 1
            break
        else:
            attempts_q4 -= 1
            print(f"Incorrect answer. You have {attempts_q4} attempts left.\n")

    if attempts_q4 == 0:
        print("You got zero points on this question. Good luck with the next question!\n")
        key += 1        

# Question 5
if key == 4:
    while attempts_q5 > 0:
        response5 = input("Question 5: What is the largest country in the world? ")
        if response5 == "Russia":
            print("Correct! You have earned 10 points.\n")
            points += 10
            print(f"Congratulations! You scored {points}/50 points in total.")
            print("Thank you for playing!")
            break
        else:
            attempts_q5 -= 1
            print(f"Incorrect answer. You have {attempts_q5} attempts left.\n")

    if attempts_q5 == 0:
        print("You got zero points on this question. Better luck next time!\n")  
        print(f"Congratulations! You scored {points}/50 points in total.")             
        print("Thank you for playing!")
        