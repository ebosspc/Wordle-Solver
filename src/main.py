'''
Credit to dwyl for providing the database of all English words
https://github.com/dwyl/english-words
'''

# Import necessary libraries and modules
import random as rand # Used for random number generation
import word_list_generation as word_list_generation # Turn the words databases into lists of lists 
import welcome as welcome # Module used to welcome the user to the program
import frequency_analysis as fqan # Import a module used for frequency analysis

# Welcome the user to the game,get their mode selection, and run the necessary setup functions
welcome.print_instructions()
welcome.mode_selection()
word_list_generation.generate_deduction_lists()
word_list_generation.get_5_letter_words_list_all_inputs()
fqan.generate_highest_net_frequency_word()
from welcome import mode_selection as mode_selection
from word_list_generation import unguessed_letters_list
from word_list_generation import known_letters_list
from word_list_generation import five_letter_words_list_all_inputs
from word_list_generation import possible_char_1_list
from word_list_generation import possible_char_2_list
from word_list_generation import possible_char_3_list
from word_list_generation import possible_char_4_list
from word_list_generation import possible_char_5_list
from frequency_analysis import highest_net_frequency_word

# Load in the proper data depending on which mode the user selected
original_five_letter_words_list = []
five_letter_words_list = []
for word in five_letter_words_list_all_inputs:
    original_five_letter_words_list.append(word)
    five_letter_words_list.append(word)
if mode_selection == 'manual':
    print("Manual selected")
if mode_selection == 'auto':
    print("Auto selected")
    first_word = highest_net_frequency_word

# Define a function that processes the first word
def process_first_word(first_word):
    # Tell the user what the first word they should enter into wordle
    print("Enter the word " + first_word.upper() + " as the your first guess.")
    print("\nPlease enter the corresponding data for each letter below:")

    # Assign variables for each of the characters in the first word and remove them from the unguessed letters list
    global word_1_char_1,word_1_char_2,word_1_char_3,word_1_char_4,word_1_char_5
    first_word_char_list = list(first_word)
    word_1_char_1 = first_word_char_list[0]
    word_1_char_2 = first_word_char_list[1]
    word_1_char_3 = first_word_char_list[2]
    word_1_char_4 = first_word_char_list[3]
    word_1_char_5 = first_word_char_list[4]
    if word_1_char_1 in unguessed_letters_list:
        unguessed_letters_list.remove(word_1_char_1)
    if word_1_char_2 in unguessed_letters_list:
        unguessed_letters_list.remove(word_1_char_2)
    if word_1_char_3 in unguessed_letters_list:
        unguessed_letters_list.remove(word_1_char_3)
    if word_1_char_4 in unguessed_letters_list:
        unguessed_letters_list.remove(word_1_char_4)
    if word_1_char_5 in unguessed_letters_list:
        unguessed_letters_list.remove(word_1_char_5)

    # Get the resulting data of the first word's first character and don't let users enter bad inputs
    while True:
        word_1_char_1_data = str(input(word_1_char_1.upper() +": "))
        if word_1_char_1_data == 'g' or word_1_char_1_data == 'y' or word_1_char_1_data == 'gr':
            break
    while True:
        word_1_char_2_data = str(input(word_1_char_2.upper() + ": "))
        if word_1_char_2_data == 'g' or word_1_char_2_data == 'y' or word_1_char_2_data == 'gr':
            break
    while True:
        word_1_char_3_data = str(input(word_1_char_3.upper() + ": "))
        if word_1_char_3_data == 'g' or word_1_char_3_data == 'y' or word_1_char_3_data == 'gr':
            break
    while True:
        word_1_char_4_data = str(input(word_1_char_4.upper() + ": "))
        if word_1_char_4_data == 'g' or word_1_char_4_data == 'y' or word_1_char_4_data == 'gr':
            break
    while True:
        word_1_char_5_data = str(input(word_1_char_5.upper() + ": "))
        if word_1_char_5_data == 'g' or word_1_char_5_data == 'y' or word_1_char_5_data == 'gr':
            break
    print("processing...")

    # Eliminate letter possibilites based on the user's inputted data
    if word_1_char_1_data == 'g':
        if word_1_char_1 in possible_char_1_list:
            possible_char_1_list.remove(word_1_char_1)
        if word_1_char_1 in possible_char_2_list:
            possible_char_2_list.remove(word_1_char_1)
        if word_1_char_1 in possible_char_3_list:
            possible_char_3_list.remove(word_1_char_1)
        if word_1_char_1 in possible_char_4_list:
            possible_char_4_list.remove(word_1_char_1)
        if word_1_char_1 in possible_char_5_list:
            possible_char_5_list.remove(word_1_char_1)
    if word_1_char_1_data == 'y':
        if word_1_char_1 in possible_char_1_list:
            possible_char_1_list.remove(word_1_char_1)
        if word_1_char_1 not in known_letters_list:
            known_letters_list.append(word_1_char_1)
    if word_1_char_1_data == 'gr':
        possible_char_1_list.clear()
        possible_char_1_list.append(word_1_char_1)
        if word_1_char_1 not in known_letters_list:
            known_letters_list.append(word_1_char_1)
    if word_1_char_2_data == 'g':
        if word_1_char_2 in possible_char_1_list:
            possible_char_1_list.remove(word_1_char_2)
        if word_1_char_2 in possible_char_2_list:
            possible_char_2_list.remove(word_1_char_2)
        if word_1_char_2 in possible_char_3_list:
            possible_char_3_list.remove(word_1_char_2)
        if word_1_char_2 in possible_char_4_list:
            possible_char_4_list.remove(word_1_char_2)
        if word_1_char_2 in possible_char_5_list:
            possible_char_5_list.remove(word_1_char_2)
    if word_1_char_2_data == 'y':
        if word_1_char_2 in possible_char_2_list:
            possible_char_2_list.remove(word_1_char_2)
        if word_1_char_2 not in known_letters_list:
            known_letters_list.append(word_1_char_2)
    if word_1_char_2_data == 'gr':
        possible_char_2_list.clear()
        possible_char_2_list.append(word_1_char_2)
        if word_1_char_2 not in known_letters_list:
            known_letters_list.append(word_1_char_2)
    if word_1_char_3_data == 'g':
        if word_1_char_3 in possible_char_1_list:
            possible_char_1_list.remove(word_1_char_3)
        if word_1_char_3 in possible_char_2_list:
            possible_char_2_list.remove(word_1_char_3)
        if word_1_char_3 in possible_char_3_list:
            possible_char_3_list.remove(word_1_char_3)
        if word_1_char_3 in possible_char_4_list:
            possible_char_4_list.remove(word_1_char_3)
        if word_1_char_3 in possible_char_5_list:
            possible_char_5_list.remove(word_1_char_3)
    if word_1_char_3_data == 'y':
        if word_1_char_3 in possible_char_3_list:
            possible_char_3_list.remove(word_1_char_3)
        if word_1_char_3 not in known_letters_list:
            known_letters_list.append(word_1_char_3)
    if word_1_char_3_data == 'gr':
        possible_char_3_list.clear()
        possible_char_3_list.append(word_1_char_3)
        if word_1_char_3 not in known_letters_list:
            known_letters_list.append(word_1_char_3)
    if word_1_char_4_data == 'g':
        if word_1_char_4 in possible_char_1_list:
            possible_char_1_list.remove(word_1_char_4)
        if word_1_char_4 in possible_char_2_list:
            possible_char_2_list.remove(word_1_char_4)
        if word_1_char_4 in possible_char_3_list:
            possible_char_3_list.remove(word_1_char_4)
        if word_1_char_4 in possible_char_4_list:
            possible_char_4_list.remove(word_1_char_4)
        if word_1_char_4 in possible_char_5_list:
            possible_char_5_list.remove(word_1_char_4)
    if word_1_char_4_data == 'y':
        if word_1_char_4 in possible_char_4_list:
            possible_char_4_list.remove(word_1_char_4)
        if word_1_char_4 not in known_letters_list:
            known_letters_list.append(word_1_char_4)
    if word_1_char_4_data == 'gr':
        possible_char_4_list.clear()
        possible_char_4_list.append(word_1_char_4)
        if word_1_char_4 not in known_letters_list:
            known_letters_list.append(word_1_char_4)
    if word_1_char_5_data == 'g':
        if word_1_char_5 in possible_char_1_list:
            possible_char_1_list.remove(word_1_char_5)
        if word_1_char_5 in possible_char_2_list:
            possible_char_2_list.remove(word_1_char_5)
        if word_1_char_5 in possible_char_3_list:
            possible_char_3_list.remove(word_1_char_5)
        if word_1_char_5 in possible_char_4_list:
            possible_char_4_list.remove(word_1_char_5)
        if word_1_char_5 in possible_char_5_list:
            possible_char_5_list.remove(word_1_char_5)
    if word_1_char_5_data == 'y':
        if word_1_char_5 in possible_char_5_list:
            possible_char_5_list.remove(word_1_char_5)
        if word_1_char_5 not in known_letters_list:
            known_letters_list.append(word_1_char_5)
    if word_1_char_5_data == 'gr':
        possible_char_5_list.clear()
        possible_char_5_list.append(word_1_char_5)
        if word_1_char_5 not in known_letters_list:
            known_letters_list.append(word_1_char_5)

    # Remove words from possibilites based on the user's inputted data
    for i in range(20): # Repeat the algorithm several times because the remove function can only remove one word at a time
        # Remove words with known impossible letters in a specific location
        for word in five_letter_words_list:
            if word[0] not in possible_char_1_list:
                five_letter_words_list.remove(word)
        for word in five_letter_words_list:
            if word[1] not in possible_char_2_list:
                five_letter_words_list.remove(word)
        for word in five_letter_words_list:
            if word[2] not in possible_char_3_list:
                five_letter_words_list.remove(word)
        for word in five_letter_words_list:
            if word[3] not in possible_char_4_list:
                five_letter_words_list.remove(word)
        for word in five_letter_words_list:
            if word[4] not in possible_char_5_list:
                five_letter_words_list.remove(word)

        # Remove words without letters that are known to be in the word
        for word in five_letter_words_list:
            for letter in known_letters_list:
                if letter not in word:
                    if word in five_letter_words_list:
                        five_letter_words_list.remove(word)

    # Select the next word to be guessed
    select_next_guess(guess_number=2)


# Define a function that processes the second word
def process_second_word(next_guess):
    # Tell the user what the first word they should enter into wordle
    print("Enter the word " + next_guess.upper() + " as the your second guess.")
    print("\nPlease enter the corresponding data for each letter below:")

    # Assign variables for each of the characters in the first word and remove them from the unguessed letters list
    global word_2_char_1,word_2_char_2,word_2_char_3,word_2_char_4,word_2_char_5
    next_guess_char_list = list(next_guess)
    word_2_char_1 = next_guess_char_list[0]
    word_2_char_2 = next_guess_char_list[1]
    word_2_char_3 = next_guess_char_list[2]
    word_2_char_4 = next_guess_char_list[3]
    word_2_char_5 = next_guess_char_list[4]
    if word_2_char_1 in unguessed_letters_list:
        unguessed_letters_list.remove(word_2_char_1)
    if word_2_char_2 in unguessed_letters_list:
        unguessed_letters_list.remove(word_2_char_2)
    if word_2_char_3 in unguessed_letters_list:
        unguessed_letters_list.remove(word_2_char_3)
    if word_2_char_4 in unguessed_letters_list:
        unguessed_letters_list.remove(word_2_char_4)
    if word_2_char_5 in unguessed_letters_list:
        unguessed_letters_list.remove(word_2_char_5)

    # Get the resulting data of the first word's first character and don't let users enter bad inputs
    while True:
        word_2_char_1_data = str(input(word_2_char_1.upper() +": "))
        if word_2_char_1_data == 'g' or word_2_char_1_data == 'y' or word_2_char_1_data == 'gr':
            break
    while True:
        word_2_char_2_data = str(input(word_2_char_2.upper() + ": "))
        if word_2_char_2_data == 'g' or word_2_char_2_data == 'y' or word_2_char_2_data == 'gr':
            break
    while True:
        word_2_char_3_data = str(input(word_2_char_3.upper() + ": "))
        if word_2_char_3_data == 'g' or word_2_char_3_data == 'y' or word_2_char_3_data == 'gr':
            break
    while True:
        word_2_char_4_data = str(input(word_2_char_4.upper() + ": "))
        if word_2_char_4_data == 'g' or word_2_char_4_data == 'y' or word_2_char_4_data == 'gr':
            break
    while True:
        word_2_char_5_data = str(input(word_2_char_5.upper() + ": "))
        if word_2_char_5_data == 'g' or word_2_char_5_data == 'y' or word_2_char_5_data == 'gr':
            break
    print("processing...")

    # Eliminate letter possibilites based on the user's inputted data
    if word_2_char_1_data == 'g':
        if word_2_char_1 in possible_char_1_list:
            possible_char_1_list.remove(word_2_char_1)
        if word_2_char_1 in possible_char_2_list:
            possible_char_2_list.remove(word_2_char_1)
        if word_2_char_1 in possible_char_3_list:
            possible_char_3_list.remove(word_2_char_1)
        if word_2_char_1 in possible_char_4_list:
            possible_char_4_list.remove(word_2_char_1)
        if word_2_char_1 in possible_char_5_list:
            possible_char_5_list.remove(word_2_char_1)
    if word_2_char_1_data == 'y':
        if word_2_char_1 in possible_char_1_list:
            possible_char_1_list.remove(word_2_char_1)
        if word_2_char_1 not in known_letters_list:
            known_letters_list.append(word_2_char_1)
    if word_2_char_1_data == 'gr':
        possible_char_1_list.clear()
        possible_char_1_list.append(word_2_char_1)
        if word_2_char_1 not in known_letters_list:
            known_letters_list.append(word_2_char_1)
    if word_2_char_2_data == 'g':
        if word_2_char_2 in possible_char_1_list:
            possible_char_1_list.remove(word_2_char_2)
        if word_2_char_2 in possible_char_2_list:
            possible_char_2_list.remove(word_2_char_2)
        if word_2_char_2 in possible_char_3_list:
            possible_char_3_list.remove(word_2_char_2)
        if word_2_char_2 in possible_char_4_list:
            possible_char_4_list.remove(word_2_char_2)
        if word_2_char_2 in possible_char_5_list:
            possible_char_5_list.remove(word_2_char_2)
    if word_2_char_2_data == 'y':
        if word_2_char_2 in possible_char_2_list:
            possible_char_2_list.remove(word_2_char_2)
        if word_2_char_2 not in known_letters_list:
            known_letters_list.append(word_2_char_2)
    if word_2_char_2_data == 'gr':
        possible_char_2_list.clear()
        possible_char_2_list.append(word_2_char_2)
        if word_2_char_2 not in known_letters_list:
            known_letters_list.append(word_2_char_2)
    if word_2_char_3_data == 'g':
        if word_2_char_3 in possible_char_1_list:
            possible_char_1_list.remove(word_2_char_3)
        if word_2_char_3 in possible_char_2_list:
            possible_char_2_list.remove(word_2_char_3)
        if word_2_char_3 in possible_char_3_list:
            possible_char_3_list.remove(word_2_char_3)
        if word_2_char_3 in possible_char_4_list:
            possible_char_4_list.remove(word_2_char_3)
        if word_2_char_3 in possible_char_5_list:
            possible_char_5_list.remove(word_2_char_3)
    if word_2_char_3_data == 'y':
        if word_2_char_3 in possible_char_3_list:
            possible_char_3_list.remove(word_2_char_3)
        if word_2_char_3 not in known_letters_list:
            known_letters_list.append(word_2_char_3)
    if word_2_char_3_data == 'gr':
        possible_char_3_list.clear()
        possible_char_3_list.append(word_2_char_3)
        if word_2_char_3 not in known_letters_list:
            known_letters_list.append(word_2_char_3)
    if word_2_char_4_data == 'g':
        if word_2_char_4 in possible_char_1_list:
            possible_char_1_list.remove(word_2_char_4)
        if word_2_char_4 in possible_char_2_list:
            possible_char_2_list.remove(word_2_char_4)
        if word_2_char_4 in possible_char_3_list:
            possible_char_3_list.remove(word_2_char_4)
        if word_2_char_4 in possible_char_4_list:
            possible_char_4_list.remove(word_2_char_4)
        if word_2_char_4 in possible_char_5_list:
            possible_char_5_list.remove(word_2_char_4)
    if word_2_char_4_data == 'y':
        if word_2_char_4 in possible_char_4_list:
            possible_char_4_list.remove(word_2_char_4)
        if word_2_char_4 not in known_letters_list:
            known_letters_list.append(word_2_char_4)
    if word_2_char_4_data == 'gr':
        possible_char_4_list.clear()
        possible_char_4_list.append(word_2_char_4)
        if word_2_char_4 not in known_letters_list:
            known_letters_list.append(word_2_char_4)
    if word_2_char_5_data == 'g':
        if word_2_char_5 in possible_char_1_list:
            possible_char_1_list.remove(word_2_char_5)
        if word_2_char_5 in possible_char_2_list:
            possible_char_2_list.remove(word_2_char_5)
        if word_2_char_5 in possible_char_3_list:
            possible_char_3_list.remove(word_2_char_5)
        if word_2_char_5 in possible_char_4_list:
            possible_char_4_list.remove(word_2_char_5)
        if word_2_char_5 in possible_char_5_list:
            possible_char_5_list.remove(word_2_char_5)
    if word_2_char_5_data == 'y':
        if word_2_char_5 in possible_char_5_list:
            possible_char_5_list.remove(word_2_char_5)
        if word_2_char_5 not in known_letters_list:
            known_letters_list.append(word_2_char_5)
    if word_2_char_5_data == 'gr':
        possible_char_5_list.clear()
        possible_char_5_list.append(word_2_char_5)
        if word_2_char_5 not in known_letters_list:
            known_letters_list.append(word_2_char_5)

    # Remove words from possibilites based on the user's inputted data
    for i in range(20):
        # Remove words with known impossible letters in a specific location
        for word in five_letter_words_list:
            if word[0] not in possible_char_1_list:
                five_letter_words_list.remove(word)
        for word in five_letter_words_list:
            if word[1] not in possible_char_2_list:
                five_letter_words_list.remove(word)
        for word in five_letter_words_list:
            if word[2] not in possible_char_3_list:
                five_letter_words_list.remove(word)
        for word in five_letter_words_list:
            if word[3] not in possible_char_4_list:
                five_letter_words_list.remove(word)
        for word in five_letter_words_list:
            if word[4] not in possible_char_5_list:
                five_letter_words_list.remove(word)

        # Remove words without letters that are known to be in the word
        for word in five_letter_words_list:
            for letter in known_letters_list:
                if letter not in word:
                    if word in five_letter_words_list:
                        five_letter_words_list.remove(word)
    
    # Select the next word to be guessed
    select_next_guess(guess_number=3)


# Define a function that processes the third word
def process_third_word(next_guess):
    # Tell the user what the first word they should enter into wordle
    print("Enter the word " + next_guess.upper() + " as the your second guess.")
    print("\nPlease enter the corresponding data for each letter below:")

    # Assign variables for each of the characters in the first word and remove them from the unguessed letters list
    global word_3_char_1,word_3_char_2,word_3_char_3,word_3_char_4,word_3_char_5
    next_guess_char_list = list(next_guess)
    word_3_char_1 = next_guess_char_list[0]
    word_3_char_2 = next_guess_char_list[1]
    word_3_char_3 = next_guess_char_list[2]
    word_3_char_4 = next_guess_char_list[3]
    word_3_char_5 = next_guess_char_list[4]
    if word_3_char_1 in unguessed_letters_list:
        unguessed_letters_list.remove(word_3_char_1)
    if word_3_char_2 in unguessed_letters_list:
        unguessed_letters_list.remove(word_3_char_2)
    if word_3_char_3 in unguessed_letters_list:
        unguessed_letters_list.remove(word_3_char_3)
    if word_3_char_4 in unguessed_letters_list:
        unguessed_letters_list.remove(word_3_char_4)
    if word_3_char_5 in unguessed_letters_list:
        unguessed_letters_list.remove(word_3_char_5)

    # Get the resulting data of the first word's first character and don't let users enter bad inputs
    while True:
        word_3_char_1_data = str(input(word_3_char_1.upper() +": "))
        if word_3_char_1_data == 'g' or word_3_char_1_data == 'y' or word_3_char_1_data == 'gr':
            break
    while True:
        word_3_char_2_data = str(input(word_3_char_2.upper() + ": "))
        if word_3_char_2_data == 'g' or word_3_char_2_data == 'y' or word_3_char_2_data == 'gr':
            break
    while True:
        word_3_char_3_data = str(input(word_3_char_3.upper() + ": "))
        if word_3_char_3_data == 'g' or word_3_char_3_data == 'y' or word_3_char_3_data == 'gr':
            break
    while True:
        word_3_char_4_data = str(input(word_3_char_4.upper() + ": "))
        if word_3_char_4_data == 'g' or word_3_char_4_data == 'y' or word_3_char_4_data == 'gr':
            break
    while True:
        word_3_char_5_data = str(input(word_3_char_5.upper() + ": "))
        if word_3_char_5_data == 'g' or word_3_char_5_data == 'y' or word_3_char_5_data == 'gr':
            break
    print("processing...")

    # Eliminate letter possibilites based on the user's inputted data
    if word_3_char_1_data == 'g':
        if word_3_char_1 in possible_char_1_list:
            possible_char_1_list.remove(word_3_char_1)
        if word_3_char_1 in possible_char_2_list:
            possible_char_2_list.remove(word_3_char_1)
        if word_3_char_1 in possible_char_3_list:
            possible_char_3_list.remove(word_3_char_1)
        if word_3_char_1 in possible_char_4_list:
            possible_char_4_list.remove(word_3_char_1)
        if word_3_char_1 in possible_char_5_list:
            possible_char_5_list.remove(word_3_char_1)
    if word_3_char_1_data == 'y':
        if word_3_char_1 in possible_char_1_list:
            possible_char_1_list.remove(word_3_char_1)
        if word_3_char_1 not in known_letters_list:
            known_letters_list.append(word_3_char_1)
    if word_3_char_1_data == 'gr':
        possible_char_1_list.clear()
        possible_char_1_list.append(word_3_char_1)
        if word_3_char_1 not in known_letters_list:
            known_letters_list.append(word_3_char_1)
    if word_3_char_2_data == 'g':
        if word_3_char_2 in possible_char_1_list:
            possible_char_1_list.remove(word_3_char_2)
        if word_3_char_2 in possible_char_2_list:
            possible_char_2_list.remove(word_3_char_2)
        if word_3_char_2 in possible_char_3_list:
            possible_char_3_list.remove(word_3_char_2)
        if word_3_char_2 in possible_char_4_list:
            possible_char_4_list.remove(word_3_char_2)
        if word_3_char_2 in possible_char_5_list:
            possible_char_5_list.remove(word_3_char_2)
    if word_3_char_2_data == 'y':
        if word_3_char_2 in possible_char_2_list:
            possible_char_2_list.remove(word_3_char_2)
        if word_3_char_2 not in known_letters_list:
            known_letters_list.append(word_3_char_2)
    if word_3_char_2_data == 'gr':
        possible_char_2_list.clear()
        possible_char_2_list.append(word_3_char_2)
        if word_3_char_2 not in known_letters_list:
            known_letters_list.append(word_3_char_2)
    if word_3_char_3_data == 'g':
        if word_3_char_3 in possible_char_1_list:
            possible_char_1_list.remove(word_3_char_3)
        if word_3_char_3 in possible_char_2_list:
            possible_char_2_list.remove(word_3_char_3)
        if word_3_char_3 in possible_char_3_list:
            possible_char_3_list.remove(word_3_char_3)
        if word_3_char_3 in possible_char_4_list:
            possible_char_4_list.remove(word_3_char_3)
        if word_3_char_3 in possible_char_5_list:
            possible_char_5_list.remove(word_3_char_3)
    if word_3_char_3_data == 'y':
        if word_3_char_3 in possible_char_3_list:
            possible_char_3_list.remove(word_3_char_3)
        if word_3_char_3 not in known_letters_list:
            known_letters_list.append(word_3_char_3)
    if word_3_char_3_data == 'gr':
        possible_char_3_list.clear()
        possible_char_3_list.append(word_3_char_3)
        if word_3_char_3 not in known_letters_list:
            known_letters_list.append(word_3_char_3)
    if word_3_char_4_data == 'g':
        if word_3_char_4 in possible_char_1_list:
            possible_char_1_list.remove(word_3_char_4)
        if word_3_char_4 in possible_char_2_list:
            possible_char_2_list.remove(word_3_char_4)
        if word_3_char_4 in possible_char_3_list:
            possible_char_3_list.remove(word_3_char_4)
        if word_3_char_4 in possible_char_4_list:
            possible_char_4_list.remove(word_3_char_4)
        if word_3_char_4 in possible_char_5_list:
            possible_char_5_list.remove(word_3_char_4)
    if word_3_char_4_data == 'y':
        if word_3_char_4 in possible_char_4_list:
            possible_char_4_list.remove(word_3_char_4)
        if word_3_char_4 not in known_letters_list:
            known_letters_list.append(word_3_char_4)
    if word_3_char_4_data == 'gr':
        possible_char_4_list.clear()
        possible_char_4_list.append(word_3_char_4)
        if word_3_char_4 not in known_letters_list:
            known_letters_list.append(word_3_char_4)
    if word_3_char_5_data == 'g':
        if word_3_char_5 in possible_char_1_list:
            possible_char_1_list.remove(word_3_char_5)
        if word_3_char_5 in possible_char_2_list:
            possible_char_2_list.remove(word_3_char_5)
        if word_3_char_5 in possible_char_3_list:
            possible_char_3_list.remove(word_3_char_5)
        if word_3_char_5 in possible_char_4_list:
            possible_char_4_list.remove(word_3_char_5)
        if word_3_char_5 in possible_char_5_list:
            possible_char_5_list.remove(word_3_char_5)
    if word_3_char_5_data == 'y':
        if word_3_char_5 in possible_char_5_list:
            possible_char_5_list.remove(word_3_char_5)
        if word_3_char_5 not in known_letters_list:
            known_letters_list.append(word_3_char_5)
    if word_3_char_5_data == 'gr':
        possible_char_5_list.clear()
        possible_char_5_list.append(word_3_char_5)
        if word_3_char_5 not in known_letters_list:
            known_letters_list.append(word_3_char_5)

    # Remove words from possibilites based on the user's inputted data
    for i in range(20):
        # Remove words with known impossible letters in a specific location
        for word in five_letter_words_list:
            if word[0] not in possible_char_1_list:
                five_letter_words_list.remove(word)
        for word in five_letter_words_list:
            if word[1] not in possible_char_2_list:
                five_letter_words_list.remove(word)
        for word in five_letter_words_list:
            if word[2] not in possible_char_3_list:
                five_letter_words_list.remove(word)
        for word in five_letter_words_list:
            if word[3] not in possible_char_4_list:
                five_letter_words_list.remove(word)
        for word in five_letter_words_list:
            if word[4] not in possible_char_5_list:
                five_letter_words_list.remove(word)

        # Remove words without letters that are known to be in the word
        for word in five_letter_words_list:
            for letter in known_letters_list:
                if letter not in word:
                    if word in five_letter_words_list:
                        five_letter_words_list.remove(word)
    
    # Select the next word to be guessed
    select_next_guess(guess_number=4)


# Define a function that process's the fourth word
def process_fourth_word(next_guess):
    # Tell the user what the first word they should enter into wordle
    print("Enter the word " + next_guess.upper() + " as the your second guess.")
    print("\nPlease enter the corresponding data for each letter below:")

    # Assign variables for each of the characters in the first word and remove them from the unguessed letters list
    global word_4_char_1,word_4_char_2,word_4_char_3,word_4_char_4,word_4_char_5
    next_guess_char_list = list(next_guess)
    word_4_char_1 = next_guess_char_list[0]
    word_4_char_2 = next_guess_char_list[1]
    word_4_char_3 = next_guess_char_list[2]
    word_4_char_4 = next_guess_char_list[3]
    word_4_char_5 = next_guess_char_list[4]
    if word_4_char_1 in unguessed_letters_list:
        unguessed_letters_list.remove(word_4_char_1)
    if word_4_char_2 in unguessed_letters_list:
        unguessed_letters_list.remove(word_4_char_2)
    if word_4_char_3 in unguessed_letters_list:
        unguessed_letters_list.remove(word_4_char_3)
    if word_4_char_4 in unguessed_letters_list:
        unguessed_letters_list.remove(word_4_char_4)
    if word_4_char_5 in unguessed_letters_list:
        unguessed_letters_list.remove(word_4_char_5)

    # Get the resulting data of the first word's first character and don't let users enter bad inputs
    while True:
        word_4_char_1_data = str(input(word_4_char_1.upper() +": "))
        if word_4_char_1_data == 'g' or word_4_char_1_data == 'y' or word_4_char_1_data == 'gr':
            break
    while True:
        word_4_char_2_data = str(input(word_4_char_2.upper() + ": "))
        if word_4_char_2_data == 'g' or word_4_char_2_data == 'y' or word_4_char_2_data == 'gr':
            break
    while True:
        word_4_char_3_data = str(input(word_4_char_3.upper() + ": "))
        if word_4_char_3_data == 'g' or word_4_char_3_data == 'y' or word_4_char_3_data == 'gr':
            break
    while True:
        word_4_char_4_data = str(input(word_4_char_4.upper() + ": "))
        if word_4_char_4_data == 'g' or word_4_char_4_data == 'y' or word_4_char_4_data == 'gr':
            break
    while True:
        word_4_char_5_data = str(input(word_4_char_5.upper() + ": "))
        if word_4_char_5_data == 'g' or word_4_char_5_data == 'y' or word_4_char_5_data == 'gr':
            break
    print("processing...")

    # Eliminate letter possibilites based on the user's inputted data
    if word_4_char_1_data == 'g':
        if word_4_char_1 in possible_char_1_list:
            possible_char_1_list.remove(word_4_char_1)
        if word_4_char_1 in possible_char_2_list:
            possible_char_2_list.remove(word_4_char_1)
        if word_4_char_1 in possible_char_3_list:
            possible_char_3_list.remove(word_4_char_1)
        if word_4_char_1 in possible_char_4_list:
            possible_char_4_list.remove(word_4_char_1)
        if word_4_char_1 in possible_char_5_list:
            possible_char_5_list.remove(word_4_char_1)
    if word_4_char_1_data == 'y':
        if word_4_char_1 in possible_char_1_list:
            possible_char_1_list.remove(word_4_char_1)
        if word_4_char_1 not in known_letters_list:
            known_letters_list.append(word_4_char_1)
    if word_4_char_1_data == 'gr':
        possible_char_1_list.clear()
        possible_char_1_list.append(word_4_char_1)
        if word_4_char_1 not in known_letters_list:
            known_letters_list.append(word_4_char_1)
    if word_4_char_2_data == 'g':
        if word_4_char_2 in possible_char_1_list:
            possible_char_1_list.remove(word_4_char_2)
        if word_4_char_2 in possible_char_2_list:
            possible_char_2_list.remove(word_4_char_2)
        if word_4_char_2 in possible_char_3_list:
            possible_char_3_list.remove(word_4_char_2)
        if word_4_char_2 in possible_char_4_list:
            possible_char_4_list.remove(word_4_char_2)
        if word_4_char_2 in possible_char_5_list:
            possible_char_5_list.remove(word_4_char_2)
    if word_4_char_2_data == 'y':
        if word_4_char_2 in possible_char_2_list:
            possible_char_2_list.remove(word_4_char_2)
        if word_4_char_2 not in known_letters_list:
            known_letters_list.append(word_4_char_2)
    if word_4_char_2_data == 'gr':
        possible_char_2_list.clear()
        possible_char_2_list.append(word_4_char_2)
        if word_4_char_2 not in known_letters_list:
            known_letters_list.append(word_4_char_2)
    if word_4_char_3_data == 'g':
        if word_4_char_3 in possible_char_1_list:
            possible_char_1_list.remove(word_4_char_3)
        if word_4_char_3 in possible_char_2_list:
            possible_char_2_list.remove(word_4_char_3)
        if word_4_char_3 in possible_char_3_list:
            possible_char_3_list.remove(word_4_char_3)
        if word_4_char_3 in possible_char_4_list:
            possible_char_4_list.remove(word_4_char_3)
        if word_4_char_3 in possible_char_5_list:
            possible_char_5_list.remove(word_4_char_3)
    if word_4_char_3_data == 'y':
        if word_4_char_3 in possible_char_3_list:
            possible_char_3_list.remove(word_4_char_3)
        if word_4_char_3 not in known_letters_list:
            known_letters_list.append(word_4_char_3)
    if word_4_char_3_data == 'gr':
        possible_char_3_list.clear()
        possible_char_3_list.append(word_4_char_3)
        if word_4_char_3 not in known_letters_list:
            known_letters_list.append(word_4_char_3)
    if word_4_char_4_data == 'g':
        if word_4_char_4 in possible_char_1_list:
            possible_char_1_list.remove(word_4_char_4)
        if word_4_char_4 in possible_char_2_list:
            possible_char_2_list.remove(word_4_char_4)
        if word_4_char_4 in possible_char_3_list:
            possible_char_3_list.remove(word_4_char_4)
        if word_4_char_4 in possible_char_4_list:
            possible_char_4_list.remove(word_4_char_4)
        if word_4_char_4 in possible_char_5_list:
            possible_char_5_list.remove(word_4_char_4)
    if word_4_char_4_data == 'y':
        if word_4_char_4 in possible_char_4_list:
            possible_char_4_list.remove(word_4_char_4)
        if word_4_char_4 not in known_letters_list:
            known_letters_list.append(word_4_char_4)
    if word_4_char_4_data == 'gr':
        possible_char_4_list.clear()
        possible_char_4_list.append(word_4_char_4)
        if word_4_char_4 not in known_letters_list:
            known_letters_list.append(word_4_char_4)
    if word_4_char_5_data == 'g':
        if word_4_char_5 in possible_char_1_list:
            possible_char_1_list.remove(word_4_char_5)
        if word_4_char_5 in possible_char_2_list:
            possible_char_2_list.remove(word_4_char_5)
        if word_4_char_5 in possible_char_3_list:
            possible_char_3_list.remove(word_4_char_5)
        if word_4_char_5 in possible_char_4_list:
            possible_char_4_list.remove(word_4_char_5)
        if word_4_char_5 in possible_char_5_list:
            possible_char_5_list.remove(word_4_char_5)
    if word_4_char_5_data == 'y':
        if word_4_char_5 in possible_char_5_list:
            possible_char_5_list.remove(word_4_char_5)
        if word_4_char_5 not in known_letters_list:
            known_letters_list.append(word_4_char_5)
    if word_4_char_5_data == 'gr':
        possible_char_5_list.clear()
        possible_char_5_list.append(word_4_char_5)
        if word_4_char_5 not in known_letters_list:
            known_letters_list.append(word_4_char_5)

    # Remove words from possibilites based on the user's inputted data
    for i in range(20):
        # Remove words with known impossible letters in a specific location
        for word in five_letter_words_list:
            if word[0] not in possible_char_1_list:
                five_letter_words_list.remove(word)
        for word in five_letter_words_list:
            if word[1] not in possible_char_2_list:
                five_letter_words_list.remove(word)
        for word in five_letter_words_list:
            if word[2] not in possible_char_3_list:
                five_letter_words_list.remove(word)
        for word in five_letter_words_list:
            if word[3] not in possible_char_4_list:
                five_letter_words_list.remove(word)
        for word in five_letter_words_list:
            if word[4] not in possible_char_5_list:
                five_letter_words_list.remove(word)

        # Remove words without letters that are known to be in the word
        for word in five_letter_words_list:
            for letter in known_letters_list:
                if letter not in word:
                    if word in five_letter_words_list:
                        five_letter_words_list.remove(word)
    
    # Select the next word to be guessed
    select_next_guess(guess_number=5)


# Define  function that process's the fifth word
def process_fifth_word(next_guess):
    # Tell the user what the first word they should enter into wordle
    print("Enter the word " + next_guess.upper() + " as the your second guess.")
    print("\nPlease enter the corresponding data for each letter below:")

    # Assign variables for each of the characters in the first word and remove them from the unguessed letters list
    global word_5_char_1,word_5_char_2,word_5_char_3,word_5_char_4,word_5_char_5
    next_guess_char_list = list(next_guess)
    word_5_char_1 = next_guess_char_list[0]
    word_5_char_2 = next_guess_char_list[1]
    word_5_char_3 = next_guess_char_list[2]
    word_5_char_4 = next_guess_char_list[3]
    word_5_char_5 = next_guess_char_list[4]
    if word_5_char_1 in unguessed_letters_list:
        unguessed_letters_list.remove(word_5_char_1)
    if word_5_char_2 in unguessed_letters_list:
        unguessed_letters_list.remove(word_5_char_2)
    if word_5_char_3 in unguessed_letters_list:
        unguessed_letters_list.remove(word_5_char_3)
    if word_5_char_4 in unguessed_letters_list:
        unguessed_letters_list.remove(word_5_char_4)
    if word_5_char_5 in unguessed_letters_list:
        unguessed_letters_list.remove(word_5_char_5)

    # Get the resulting data of the first word's first character and don't let users enter bad inputs
    while True:
        word_5_char_1_data = str(input(word_5_char_1.upper() +": "))
        if word_5_char_1_data == 'g' or word_5_char_1_data == 'y' or word_5_char_1_data == 'gr':
            break
    while True:
        word_5_char_2_data = str(input(word_5_char_2.upper() + ": "))
        if word_5_char_2_data == 'g' or word_5_char_2_data == 'y' or word_5_char_2_data == 'gr':
            break
    while True:
        word_5_char_3_data = str(input(word_5_char_3.upper() + ": "))
        if word_5_char_3_data == 'g' or word_5_char_3_data == 'y' or word_5_char_3_data == 'gr':
            break
    while True:
        word_5_char_4_data = str(input(word_5_char_4.upper() + ": "))
        if word_5_char_4_data == 'g' or word_5_char_4_data == 'y' or word_5_char_4_data == 'gr':
            break
    while True:
        word_5_char_5_data = str(input(word_5_char_5.upper() + ": "))
        if word_5_char_5_data == 'g' or word_5_char_5_data == 'y' or word_5_char_5_data == 'gr':
            break
    print("processing...")

    # Eliminate letter possibilites based on the user's inputted data
    if word_5_char_1_data == 'g':
        if word_5_char_1 in possible_char_1_list:
            possible_char_1_list.remove(word_5_char_1)
        if word_5_char_1 in possible_char_2_list:
            possible_char_2_list.remove(word_5_char_1)
        if word_5_char_1 in possible_char_3_list:
            possible_char_3_list.remove(word_5_char_1)
        if word_5_char_1 in possible_char_4_list:
            possible_char_4_list.remove(word_5_char_1)
        if word_5_char_1 in possible_char_5_list:
            possible_char_5_list.remove(word_5_char_1)
    if word_5_char_1_data == 'y':
        if word_5_char_1 in possible_char_1_list:
            possible_char_1_list.remove(word_5_char_1)
        if word_5_char_1 not in known_letters_list:
            known_letters_list.append(word_5_char_1)
    if word_5_char_1_data == 'gr':
        possible_char_1_list.clear()
        possible_char_1_list.append(word_5_char_1)
        if word_5_char_1 not in known_letters_list:
            known_letters_list.append(word_5_char_1)
    if word_5_char_2_data == 'g':
        if word_5_char_2 in possible_char_1_list:
            possible_char_1_list.remove(word_5_char_2)
        if word_5_char_2 in possible_char_2_list:
            possible_char_2_list.remove(word_5_char_2)
        if word_5_char_2 in possible_char_3_list:
            possible_char_3_list.remove(word_5_char_2)
        if word_5_char_2 in possible_char_4_list:
            possible_char_4_list.remove(word_5_char_2)
        if word_5_char_2 in possible_char_5_list:
            possible_char_5_list.remove(word_5_char_2)
    if word_5_char_2_data == 'y':
        if word_5_char_2 in possible_char_2_list:
            possible_char_2_list.remove(word_5_char_2)
        if word_5_char_2 not in known_letters_list:
            known_letters_list.append(word_5_char_2)
    if word_5_char_2_data == 'gr':
        possible_char_2_list.clear()
        possible_char_2_list.append(word_5_char_2)
        if word_5_char_2 not in known_letters_list:
            known_letters_list.append(word_5_char_2)
    if word_5_char_3_data == 'g':
        if word_5_char_3 in possible_char_1_list:
            possible_char_1_list.remove(word_5_char_3)
        if word_5_char_3 in possible_char_2_list:
            possible_char_2_list.remove(word_5_char_3)
        if word_5_char_3 in possible_char_3_list:
            possible_char_3_list.remove(word_5_char_3)
        if word_5_char_3 in possible_char_4_list:
            possible_char_4_list.remove(word_5_char_3)
        if word_5_char_3 in possible_char_5_list:
            possible_char_5_list.remove(word_5_char_3)
    if word_5_char_3_data == 'y':
        if word_5_char_3 in possible_char_3_list:
            possible_char_3_list.remove(word_5_char_3)
        if word_5_char_3 not in known_letters_list:
            known_letters_list.append(word_5_char_3)
    if word_5_char_3_data == 'gr':
        possible_char_3_list.clear()
        possible_char_3_list.append(word_5_char_3)
        if word_5_char_3 not in known_letters_list:
            known_letters_list.append(word_5_char_3)
    if word_5_char_4_data == 'g':
        if word_5_char_4 in possible_char_1_list:
            possible_char_1_list.remove(word_5_char_4)
        if word_5_char_4 in possible_char_2_list:
            possible_char_2_list.remove(word_5_char_4)
        if word_5_char_4 in possible_char_3_list:
            possible_char_3_list.remove(word_5_char_4)
        if word_5_char_4 in possible_char_4_list:
            possible_char_4_list.remove(word_5_char_4)
        if word_5_char_4 in possible_char_5_list:
            possible_char_5_list.remove(word_5_char_4)
    if word_5_char_4_data == 'y':
        if word_5_char_4 in possible_char_4_list:
            possible_char_4_list.remove(word_5_char_4)
        if word_5_char_4 not in known_letters_list:
            known_letters_list.append(word_5_char_4)
    if word_5_char_4_data == 'gr':
        possible_char_4_list.clear()
        possible_char_4_list.append(word_5_char_4)
        if word_5_char_4 not in known_letters_list:
            known_letters_list.append(word_5_char_4)
    if word_5_char_5_data == 'g':
        if word_5_char_5 in possible_char_1_list:
            possible_char_1_list.remove(word_5_char_5)
        if word_5_char_5 in possible_char_2_list:
            possible_char_2_list.remove(word_5_char_5)
        if word_5_char_5 in possible_char_3_list:
            possible_char_3_list.remove(word_5_char_5)
        if word_5_char_5 in possible_char_4_list:
            possible_char_4_list.remove(word_5_char_5)
        if word_5_char_5 in possible_char_5_list:
            possible_char_5_list.remove(word_5_char_5)
    if word_5_char_5_data == 'y':
        if word_5_char_5 in possible_char_5_list:
            possible_char_5_list.remove(word_5_char_5)
        if word_5_char_5 not in known_letters_list:
            known_letters_list.append(word_5_char_5)
    if word_5_char_5_data == 'gr':
        possible_char_5_list.clear()
        possible_char_5_list.append(word_5_char_5)
        if word_5_char_5 not in known_letters_list:
            known_letters_list.append(word_5_char_5)

    # Remove words from possibilites based on the user's inputted data
    for i in range(20):
        # Remove words with known impossible letters in a specific location
        for word in five_letter_words_list:
            if word[0] not in possible_char_1_list:
                five_letter_words_list.remove(word)
        for word in five_letter_words_list:
            if word[1] not in possible_char_2_list:
                five_letter_words_list.remove(word)
        for word in five_letter_words_list:
            if word[2] not in possible_char_3_list:
                five_letter_words_list.remove(word)
        for word in five_letter_words_list:
            if word[3] not in possible_char_4_list:
                five_letter_words_list.remove(word)
        for word in five_letter_words_list:
            if word[4] not in possible_char_5_list:
                five_letter_words_list.remove(word)

        # Remove words without letters that are known to be in the word
        for word in five_letter_words_list:
            for letter in known_letters_list:
                if letter not in word:
                    if word in five_letter_words_list:
                        five_letter_words_list.remove(word)
    
    # Select the next word to be guessed
    select_next_guess(guess_number=6)


# Define a function that runs an algorithm to select the next best possible guess
def select_next_guess(guess_number):
    global next_guess
    if guess_number == 1:
        ...
    # Define variables to track word sorting
    best_word = ['',0]
    current_score = 0

    # Sort each word based on how many characters it has in that haven't been guess yet
    for word in original_five_letter_words_list:
        if word[0] in unguessed_letters_list:
            current_score += 1
        if len(possible_char_1_list) == 1:
            if word[0] in possible_char_1_list:
                current_score -= 0.5
        if word[1] in unguessed_letters_list:
            current_score += 1
        if len(possible_char_2_list) == 1:
            if word[1] in possible_char_2_list:
                current_score -= 0.5
        if word[2] in unguessed_letters_list:
            current_score += 1
        if len(possible_char_3_list) == 1:
            if word[2] in possible_char_3_list:
                current_score -= 0.5
        if word[3] in unguessed_letters_list:
            current_score += 1
        if len(possible_char_4_list) == 1:
            if word[3] in possible_char_4_list:
                current_score -= 0.5
        if word[4] in unguessed_letters_list:
            current_score += 1
        if len(possible_char_5_list) == 1:
            if word[4] in possible_char_5_list:
                current_score -= 0.5
        current_score = current_score -(len(list(word))-len(set(word))) # Subtracts the number of repeated letters

        # Updates the best word tracker
        if current_score >= best_word[1]:
            best_word.clear()
            best_word.append(word)
            best_word.append(current_score)
        current_score = 0

    # Extract the best word from the sorting algorithm
    if best_word[1] > 0:
        next_guess = best_word[0]
    else:
        print("No more unused characters, random word from possible words chosen.")
        if len(five_letter_words_list) == 0:
            print("Sorry there are no possible word combinations with the data you entered")
            quit()


process_first_word(first_word)
if len(five_letter_words_list) == 1:
    print(five_letter_words_list)
    quit()
process_second_word(next_guess)
if len(five_letter_words_list) == 1:
    print(five_letter_words_list)
    quit()
process_third_word(next_guess)
if len(five_letter_words_list) == 1:
    print(five_letter_words_list)
    quit()
process_fourth_word(next_guess)
if len(five_letter_words_list) == 1:
    print(five_letter_words_list)
    quit()
process_fifth_word(next_guess)
print(five_letter_words_list)
quit()
