# Ask User if they played before
show_instructions= input(print("would you like to play the maths quiz before")).lower()

# If Yes output program continues
if show_instructions.lower() == "yes":
    print("Program continues")

elif show_instructions.lower() == "y":
    print("Program continues")

# If no output exit program
elif show_instructions.lower() == "no":
    print("exit program")

elif show_instructions.lower() == "n":
    print("exit program")

else:print("Please answer with yes and no ")





