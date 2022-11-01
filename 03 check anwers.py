import random

score = 0
questions_asked = 0
while questions_asked != 12:
    num1 = 9
    num2 = random.randint(2, 12)

    answer = num1*num2
    question = int(input(f"{num1} x {num2} = "))

    if question == answer:
        print("Correct ")
        score += 10
        questions_asked += 1
    else:
        print("Incorrect.")
        score -= 10
        questions_asked += 1

    print(f"Score: {score}")
    
