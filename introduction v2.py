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
