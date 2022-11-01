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
