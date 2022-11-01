import random

# Function go here...
Valid = False

show_instructions = ""

while Valid == False and show_instructions.lower() != "xxx":
    # Ask user if they ever played before
    show_instructions = input("will you like to do a maths quiz").lower()

    # If yes output 'display instructions'
    if show_instructions.lower() == "yes" or show_instructions == "y":
        print("Program continues")
        Valid = True
    # If no output 'display instructions'
    elif Valid == False and show_instructions.lower() == "no" or show_instructions == "n":
        print("Exit program")

        Valid = True
    else:
        print("Please enter yes or no")


Valid = False

show_instructions = ""

while Valid == False and show_instructions.lower() != "xxx":
    # Ask user if they ever played before
    show_instructions = input("Have you ever played the maths quiz before").lower()

    # If yes output 'display instructions'
    if show_instructions.lower() == "yes" or show_instructions == "y":
        print("Program continues")
        Valid = True
    # If no output 'display instructions'
    elif Valid == False and show_instructions.lower() == "no" or show_instructions == "n":
        print("This is a quiz where we will challenge your 9 times tables in a random order.")
        print("Try getting as many as you can right ")
        Valid = True
    else:
        print("Please enter yes or no")


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
