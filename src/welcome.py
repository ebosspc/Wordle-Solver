# Define a function to print instructions for the game
def print_instructions():
    # Welcome the user and ask them if they want to see the instructions
    print("Welcome to the Wordle solver tool!")
    instructions_request = str(input("Would you like to view the instructions? Type y for yes, no for no: "))

    # Print the instructions if the user wants to see them
    if instructions_request == 'y':
        print("\nThis program will guide you through consistently, accurately, and effectively solving Wordle Puzzles.")
        print("The program will prompt you to enter a word as a guess into wordle,\nthen ask you to input the results character by character.")
        print("If the character doesn't exist in the word by showing up grey in wordle please type the letter g in the terminal with its corresponding letter.")
        print("If the character exists in the word by showing up as yellow in wordle please type the letter y in the terminal with its coresponding letter.")
        print("If the character exists in the word and is in the right place by showing up as green in wordle, please type the letters gr with its corresponding letter.")


# Define a function that selects the mode that the user wants to use in the algorithm
def mode_selection():
    global mode_selection
    while True:
        mode_selection = str(input("Please select which mode you would like to use this algorithm in.\nType m for manual or a for automatic: "))
        if mode_selection == 'm' or mode_selection == 'a':
            if mode_selection == 'm':
                mode_selection = 'manual'
            if mode_selection == 'a':
                mode_selection = 'auto'
            break
        else:
            print("Sorry that was an invalid input. Please try again.")

# Define a function that selects the game difficulty that the user wants to use
def game_difficulty():
    global game_difficulty
    while True:
        game_difficulty = str(input("Please select the difficulty you are playing on.\nType e for easy or h for hard: "))
        if game_difficulty == 'e' or game_difficulty == 'h':
            if game_difficulty == 'e':
                game_difficulty = 'easy'
            if game_difficulty == 'h':
                game_difficulty = 'hard'
            break
        else:
            print("Sorry that was an invalid input. Please try again.")
    ...
