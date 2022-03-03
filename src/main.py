'''
Credit to dwyl for providing the database of all English words
https://github.com/dwyl/english-words

Credit to tabatkins for providing the txt file of all possible Wordle inputs
https://github.com/tabatkins/wordle-list
'''

# Import necessary libraries and modules
import random as rand # Used for random number generation
import word_list_generation as word_list_generation # Turn the words databases into lists of lists 
import welcome as welcome # Module used to welcome the user to the program
import word_processing as word_processing # Import a module used to process word data
import frequency_analysis as fqan # Import a module used for frequency analysis

# Welcome the user to the game,get their mode selection, and run the necessary setup functions
welcome.print_instructions()
welcome.mode_selection()
word_list_generation.generate_deduction_lists()
word_list_generation.get_5_letter_words_list_all_words()
fqan.generate_highest_net_frequency_word()
from welcome import mode_selection as mode_selection
from word_list_generation import unguessed_letters_list
from word_list_generation import known_letters_list
from word_list_generation import five_letter_words_list_all_words
from word_list_generation import possible_char_1_list
from word_list_generation import possible_char_2_list
from word_list_generation import possible_char_3_list
from word_list_generation import possible_char_4_list
from word_list_generation import possible_char_5_list
from frequency_analysis import highest_net_frequency_word

# Load in the proper data depending on which mode the user selected
original_five_letter_words_list = five_letter_words_list_all_words
five_letter_words_list = five_letter_words_list_all_words
if mode_selection == 'manual':
    print("Manual selected")
if mode_selection == 'auto':
    print("Auto selected")
    first_word = highest_net_frequency_word


# Define a function that takes inputted data as parameter and returns the results
def process_first_word(first_word):
    # Tell the user what the first word they should enter into wordle
    print("Enter the word " + first_word.upper() + " as the your first guess.")
    print("\nPlease enter the corresponding data for each letter below:")

    # Assign variables for each of the characters in the first word and remove them from the unguessed letters list
    global first_word_char_list,word_1_char_1,word_1_char_2,word_1_char_3,word_1_char_4,word_1_char_5
    first_word_char_list = list(first_word)
    word_1_char_1 = first_word_char_list[0]
    word_1_char_2 = first_word_char_list[1]
    word_1_char_3 = first_word_char_list[2]
    word_1_char_4 = first_word_char_list[3]
    word_1_char_5 = first_word_char_list[4]
    unguessed_letters_list.remove(word_1_char_1)
    unguessed_letters_list.remove(word_1_char_2)
    unguessed_letters_list.remove(word_1_char_3)
    unguessed_letters_list.remove(word_1_char_4)
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


def select_next_guess(unguessed_letters_list,guess_number):
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
        if word[1] in unguessed_letters_list:
            current_score += 1
        if word[2] in unguessed_letters_list:
            current_score += 1
        if word[3] in unguessed_letters_list:
            current_score += 1
        if word[4] in unguessed_letters_list:
            current_score += 1
        current_score = current_score -(len(list(word))-len(set(word)))
        if current_score > best_word[1]:
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
select_next_guess(unguessed_letters_list,guess_number=2)
print(five_letter_words_list)
print(next_guess)



# Generate a list of all 5 letter words in English and import it
#word_list_generation.get_5_letter_words()
#from word_list_generation import five_letter_words_list
#original_five_letter_word_list = five_letter_words_list

'''
#####-Functions-#####
# Define a function to remove impossible words after the first guess
def remove_first_guess_words():
    # Get the first word's data and import it into this module
    word_processing.get_first_word_data()
    word_processing.process_first_word_data()
    global five_letter_words_list,known_letters_list,possible_char_1_list,possible_char_2_list,possible_char_3_list,possible_char_4_list,possible_char_5_list
    from word_processing import possible_char_1_list
    from word_processing import possible_char_2_list
    from word_processing import possible_char_3_list
    from word_processing import possible_char_4_list
    from word_processing import possible_char_5_list
    from word_processing import known_letters_list

    # Remove eliminated words from the possible words list
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


# Define a function to remove impossible words after the second guess
def remove_second_guess_words():
    # Get the second word's data and import it into this module
    word_processing.get_second_word_data()
    word_processing.process_second_word_data()
    global five_letter_words_list, known_letters_list
    from word_processing import possible_char_1_list
    from word_processing import possible_char_2_list
    from word_processing import possible_char_3_list
    from word_processing import possible_char_4_list
    from word_processing import possible_char_5_list
    from word_processing import known_letters_list 
    # Remove eliminated words from the possible words list
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
    
    # Remove any words missed the first time
    remove_unremoved_words(guess_number=2)


# Define a function to remove words that should have been removed but didn't
def remove_unremoved_words(guess_number):
    global five_letter_words_list
    for i in range(20):
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


# Define a function to determine the best thrid word that the user shoudl guess
def grab_third_word():
    global unguessed_letters_list,best_word_char_1,best_word_char_2,best_word_char_3,best_word_char_4,best_word_char_5
    unguessed_letters_list = ['b','f','g','h','j','k','m','n','p','q','r','t','v','w','x','y','z']

    # Define variables to track word sorting
    best_word = ['',0]
    current_score = 0

    # Sort each word based on how many characters it has in that haven't been guess yet
    for word in original_five_letter_word_list:
        if word[0] in unguessed_letters_list:
            current_score += 1
        if word[1] in unguessed_letters_list:
            current_score += 1
        if word[2] in unguessed_letters_list:
            current_score += 1
        if word[3] in unguessed_letters_list:
            current_score += 1
        if word[4] in unguessed_letters_list:
            current_score += 1
        if current_score > best_word[1]:
            best_word.clear()
            best_word.append(word)
            best_word.append(current_score)
        current_score = 0

    # Extract the best word from the sorting algorithm
    if best_word[1] > 0:
        best_word = best_word[0]
    else:
        print("No more unused characters, random word from possible words chosen.")
        if len(five_letter_words_list) == 0:
            print("Sorry there are no possible word combinations with the data you entered")
            quit()
        else:
            best_word = rand.choice(five_letter_words_list)

    # Split up the best word into 5 variables, each containing one of its characters
    best_word_char_1 = best_word[0]
    if best_word_char_1 in unguessed_letters_list:
        unguessed_letters_list.remove(best_word_char_1)
    best_word_char_2 = best_word[1]
    if best_word_char_2 in unguessed_letters_list:
        unguessed_letters_list.remove(best_word_char_2)
    best_word_char_3 = best_word[2]
    if best_word_char_3 in unguessed_letters_list:
        unguessed_letters_list.remove(best_word_char_3)
    best_word_char_4 = best_word[3]
    if best_word_char_4 in unguessed_letters_list:
        unguessed_letters_list.remove(best_word_char_4)
    best_word_char_5 = best_word[4]
    if best_word_char_5 in unguessed_letters_list:
        unguessed_letters_list.remove(best_word_char_5)  


# Defune a function to remove impossible words after the third guess
def remove_third_guess_words():
    # Get the best third word to guess
    grab_third_word()

    # Globalize data variables that will be used in other modules
    global word_3_char_1_data,word_3_char_2_data,word_3_char_3_data,word_3_char_4_data,word_3_char_5_data

    # Tell the user what the first word they should enter into wordle
    print("Enter the word", best_word_char_1+best_word_char_2+best_word_char_3+best_word_char_4+best_word_char_5, "as the your third guess.")
    print("\nPlease enter the corresponding data for each letter below:")

    # Get the resulting data of the first word's first character and don't let users enter bad inputs
    while True:
        word_3_char_1_data = str(input(best_word_char_1 + ": "))
        if word_3_char_1_data == 'g' or word_3_char_1_data == 'y' or word_3_char_1_data == 'gr':
            break
    while True:
        word_3_char_2_data = str(input(best_word_char_2 + ": "))
        if word_3_char_2_data == 'g' or word_3_char_2_data == 'y' or word_3_char_2_data == 'gr':
            break
    while True:
        word_3_char_3_data = str(input(best_word_char_3 + ": "))
        if word_3_char_3_data == 'g' or word_3_char_3_data == 'y' or word_3_char_3_data == 'gr':
            break
    while True:
        word_3_char_4_data = str(input(best_word_char_4 + ": "))
        if word_3_char_4_data == 'g' or word_3_char_4_data == 'y' or word_3_char_4_data == 'gr':
            break
    while True:
        word_3_char_5_data = str(input(best_word_char_5 + ": "))
        if word_3_char_5_data == 'g' or word_3_char_5_data == 'y' or word_3_char_5_data == 'gr':
            break
    
    # Out put a mesage to the user that their data is being processed
    print("processing...")
    
    # Create globalized lists that contain the possible letters a specific character in the word can be
    global possible_char_1_list,possible_char_2_list,possible_char_3_list,possible_char_4_list,possible_char_5_list

    # Eliminate letter possibilites based on the user's inputted data
    if word_3_char_1_data == 'g':
        if best_word_char_1 in possible_char_1_list:
            possible_char_1_list.remove(best_word_char_1)
        if best_word_char_1 in possible_char_2_list:
            possible_char_2_list.remove(best_word_char_1)
        if best_word_char_1 in possible_char_3_list:
            possible_char_3_list.remove(best_word_char_1)
        if best_word_char_1 in possible_char_4_list:
            possible_char_4_list.remove(best_word_char_1)
        if best_word_char_1 in possible_char_5_list:
            possible_char_5_list.remove(best_word_char_1)
    if word_3_char_1_data == 'y':
        if best_word_char_1 in possible_char_1_list:
            possible_char_1_list.remove(best_word_char_1)
        if best_word_char_1 not in known_letters_list:
            known_letters_list.append(best_word_char_1)
    if word_3_char_1_data == 'gr':
        possible_char_1_list.clear()
        possible_char_1_list.append(best_word_char_1)
        if best_word_char_1 not in known_letters_list:
            known_letters_list.append(best_word_char_1)
    
    # Eliminate letter possibilites based on the user's inputted data
    if word_3_char_2_data == 'g':
        if best_word_char_2 in possible_char_1_list:
            possible_char_1_list.remove(best_word_char_2)
        if best_word_char_2 in possible_char_2_list:
            possible_char_2_list.remove(best_word_char_2)
        if best_word_char_2 in possible_char_3_list:
            possible_char_3_list.remove(best_word_char_2)
        if best_word_char_2 in possible_char_4_list:
            possible_char_4_list.remove(best_word_char_2)
        if best_word_char_2 in possible_char_5_list:
            possible_char_5_list.remove(best_word_char_2)
    if word_3_char_2_data == 'y':
        if best_word_char_2 in possible_char_2_list:
            possible_char_2_list.remove(best_word_char_2)
        if best_word_char_2 not in known_letters_list:
            known_letters_list.append(best_word_char_2)
    if word_3_char_2_data == 'gr':
        possible_char_2_list.clear()
        possible_char_2_list.append(best_word_char_2)
        if best_word_char_2 not in known_letters_list:
            known_letters_list.append(best_word_char_2)


    # Eliminate letter possibilites based on the user's inputted data
    if word_3_char_3_data == 'g':
        if best_word_char_3 in possible_char_1_list:
            possible_char_1_list.remove(best_word_char_3)
        if best_word_char_3 in possible_char_2_list:
            possible_char_2_list.remove(best_word_char_3)
        if best_word_char_3 in possible_char_3_list:
            possible_char_3_list.remove(best_word_char_3)
        if best_word_char_3 in possible_char_4_list:
            possible_char_4_list.remove(best_word_char_3)
        if best_word_char_3 in possible_char_5_list:
            possible_char_5_list.remove(best_word_char_3)
    if word_3_char_3_data == 'y':
        if best_word_char_3 in possible_char_3_list:
            possible_char_3_list.remove(best_word_char_3)
        if best_word_char_3 not in known_letters_list:
            known_letters_list.append(best_word_char_3)
    if word_3_char_3_data == 'gr':
        possible_char_3_list.clear()
        possible_char_3_list.append(best_word_char_3)
        if best_word_char_3 not in known_letters_list:
            known_letters_list.append(best_word_char_3)

    # Eliminate letter possibilites based on the user's inputted data
    if word_3_char_4_data == 'g':
        if best_word_char_4 in possible_char_1_list:
            possible_char_1_list.remove(best_word_char_4)
        if best_word_char_4 in possible_char_2_list:
            possible_char_2_list.remove(best_word_char_4)
        if best_word_char_4 in possible_char_3_list:
            possible_char_3_list.remove(best_word_char_4)
        if best_word_char_4 in possible_char_4_list:
            possible_char_4_list.remove(best_word_char_4)
        if best_word_char_4 in possible_char_5_list:
            possible_char_5_list.remove(best_word_char_4)
    if word_3_char_4_data == 'y':
        if best_word_char_4 in possible_char_4_list:
            possible_char_4_list.remove(best_word_char_4)
        if best_word_char_4 not in known_letters_list:
            known_letters_list.append(best_word_char_4)
    if word_3_char_4_data == 'gr':
        possible_char_4_list.clear()
        possible_char_4_list.append(best_word_char_4)
        if best_word_char_4 not in known_letters_list:
            known_letters_list.append(best_word_char_4)

    # Eliminate letter possibilites based on the user's inputted data
    if word_3_char_5_data == 'g':
        if best_word_char_5 in possible_char_1_list:
            possible_char_1_list.remove(best_word_char_5)
        if best_word_char_5 in possible_char_2_list:
            possible_char_2_list.remove(best_word_char_5)
        if best_word_char_5 in possible_char_3_list:
            possible_char_3_list.remove(best_word_char_5)
        if best_word_char_5 in possible_char_4_list:
            possible_char_4_list.remove(best_word_char_5)
        if best_word_char_5 in possible_char_5_list:
            possible_char_5_list.remove(best_word_char_5)
    if word_3_char_5_data == 'y':
        if best_word_char_5 in possible_char_5_list:
            possible_char_5_list.remove(best_word_char_5)
        if best_word_char_5 not in known_letters_list:
            known_letters_list.append(best_word_char_5)
    if word_3_char_5_data == 'gr':
        possible_char_5_list.clear()
        possible_char_5_list.append(best_word_char_5)
        if best_word_char_5 not in known_letters_list:
            known_letters_list.append(best_word_char_5)
    
    # Remove words that no longer fit the possible character lists
    remove_unremoved_words(guess_number=3)


# Define a function to determine the best fourth word that the user should guess
def grab_fourth_word():
    global best_word_char_1,best_word_char_2,best_word_char_3,best_word_char_4,best_word_char_5
    # Define variables to track word sorting
    best_word = ['',0]
    current_score = 0

    # Sort each word based on how many characters it has in that haven't been guess yet
    for word in original_five_letter_word_list:
        if word[0] in unguessed_letters_list:
            current_score += 1
        if word[1] in unguessed_letters_list:
            current_score += 1
        if word[2] in unguessed_letters_list:
            current_score += 1
        if word[3] in unguessed_letters_list:
            current_score += 1
        if word[4] in unguessed_letters_list:
            current_score += 1
        if current_score > best_word[1]:
            best_word.clear()
            best_word.append(word)
            best_word.append(current_score)
        current_score = 0

    # Extract the best word from the sorting algorithm
    if best_word[1] > 0:
        best_word = best_word[0]
    else:
        print("No more unused characters, random word from possible words chosen.")
        if len(five_letter_words_list) == 0:
            print("Sorry there are no possible word combinations with the data you entered")
            quit()
        else:
            best_word = rand.choice(five_letter_words_list)

    # Split up the best word into 5 variables, each containing one of its characters
    best_word_char_1 = best_word[0]
    if best_word_char_1 in unguessed_letters_list:
        unguessed_letters_list.remove(best_word_char_1)
    best_word_char_2 = best_word[1]
    if best_word_char_2 in unguessed_letters_list:
        unguessed_letters_list.remove(best_word_char_2)
    best_word_char_3 = best_word[2]
    if best_word_char_3 in unguessed_letters_list:
        unguessed_letters_list.remove(best_word_char_3)
    best_word_char_4 = best_word[3]
    if best_word_char_4 in unguessed_letters_list:
        unguessed_letters_list.remove(best_word_char_4)
    best_word_char_5 = best_word[4]
    if best_word_char_5 in unguessed_letters_list:
        unguessed_letters_list.remove(best_word_char_5)


# Defune a function to remove impossible words after the fourth guess
def remove_fourth_guess_words():
    grab_fourth_word()

    # Globalize data variables that will be used in other modules
    global word_4_char_1_data,word_4_char_2_data,word_4_char_3_data,word_4_char_4_data,word_4_char_5_data

    # Tell the user what the first word they should enter into wordle
    print("Enter the word", best_word_char_1+best_word_char_2+best_word_char_3+best_word_char_4+best_word_char_5, "as  your fourth guess.")
    print("\nPlease enter the corresponding data for each letter below:")

    # Get the resulting data of the first word's characters and don't let users enter bad inputs
    while True:
        word_4_char_1_data = str(input(best_word_char_1 + ": "))
        if word_4_char_1_data == 'g' or word_4_char_1_data == 'y' or word_4_char_1_data == 'gr':
            break
    while True:
        word_4_char_2_data = str(input(best_word_char_2 + ": "))
        if word_4_char_2_data == 'g' or word_4_char_2_data == 'y' or word_4_char_2_data == 'gr':
            break
    while True:
        word_4_char_3_data = str(input(best_word_char_3 + ": "))
        if word_4_char_3_data == 'g' or word_4_char_3_data == 'y' or word_4_char_3_data == 'gr':
            break
    while True:
        word_4_char_4_data = str(input(best_word_char_4 + ": "))
        if word_4_char_4_data == 'g' or word_4_char_4_data == 'y' or word_4_char_4_data == 'gr':
            break
    while True:
        word_4_char_5_data = str(input(best_word_char_5 + ": "))
        if word_4_char_5_data == 'g' or word_4_char_5_data == 'y' or word_4_char_5_data == 'gr':
            break
    
    # Output a mesage to the user that their data is being processed
    print("processing...")
    
    # Create globalized lists that contain the possible letters a specific character in the word can be
    global possible_char_1_list,possible_char_2_list,possible_char_3_list,possible_char_4_list,possible_char_5_list

    # Eliminate letter possibilites based on the user's inputted data
    if word_4_char_1_data == 'g':
        if best_word_char_1 in possible_char_1_list:
            possible_char_1_list.remove(best_word_char_1)
        if best_word_char_1 in possible_char_2_list:
            possible_char_2_list.remove(best_word_char_1)
        if best_word_char_1 in possible_char_3_list:
            possible_char_3_list.remove(best_word_char_1)
        if best_word_char_1 in possible_char_4_list:
            possible_char_4_list.remove(best_word_char_1)
        if best_word_char_1 in possible_char_5_list:
            possible_char_5_list.remove(best_word_char_1)
    if word_4_char_1_data == 'y':
        if best_word_char_1 in possible_char_1_list:
            possible_char_1_list.remove(best_word_char_1)
        if best_word_char_1 not in known_letters_list:
            known_letters_list.append(best_word_char_1)
    if word_4_char_1_data == 'gr':
        possible_char_1_list.clear()
        possible_char_1_list.append(best_word_char_1)
        if best_word_char_1 not in known_letters_list:
            known_letters_list.append(best_word_char_1)
    
    # Eliminate letter possibilites based on the user's inputted data
    if word_4_char_2_data == 'g':
        if best_word_char_2 in possible_char_1_list:
            possible_char_1_list.remove(best_word_char_2)
        if best_word_char_2 in possible_char_2_list:
            possible_char_2_list.remove(best_word_char_2)
        if best_word_char_2 in possible_char_3_list:
            possible_char_3_list.remove(best_word_char_2)
        if best_word_char_2 in possible_char_4_list:
            possible_char_4_list.remove(best_word_char_2)
        if best_word_char_2 in possible_char_5_list:
            possible_char_5_list.remove(best_word_char_2)
    if word_4_char_2_data == 'y':
        if best_word_char_2 in possible_char_2_list:
            possible_char_2_list.remove(best_word_char_2)
        if best_word_char_2 not in known_letters_list:
            known_letters_list.append(best_word_char_2)
    if word_4_char_2_data == 'gr':
        possible_char_2_list.clear()
        possible_char_2_list.append(best_word_char_2)
        if best_word_char_2 not in known_letters_list:
            known_letters_list.append(best_word_char_2)

    # Eliminate letter possibilites based on the user's inputted data
    if word_4_char_3_data == 'g':
        if best_word_char_3 in possible_char_1_list:
            possible_char_1_list.remove(best_word_char_3)
        if best_word_char_3 in possible_char_2_list:
            possible_char_2_list.remove(best_word_char_3)
        if best_word_char_3 in possible_char_3_list:
            possible_char_3_list.remove(best_word_char_3)
        if best_word_char_3 in possible_char_4_list:
            possible_char_4_list.remove(best_word_char_3)
        if best_word_char_3 in possible_char_5_list:
            possible_char_5_list.remove(best_word_char_3)
    if word_4_char_3_data == 'y':
        if best_word_char_3 in possible_char_3_list:
            possible_char_3_list.remove(best_word_char_3)
        if best_word_char_3 not in known_letters_list:
            known_letters_list.append(best_word_char_3)
    if word_4_char_3_data == 'gr':
        possible_char_3_list.clear()
        possible_char_3_list.append(best_word_char_3)
        if best_word_char_3 not in known_letters_list:
            known_letters_list.append(best_word_char_3)

    # Eliminate letter possibilites based on the user's inputted data
    if word_4_char_4_data == 'g':
        if best_word_char_4 in possible_char_1_list:
            possible_char_1_list.remove(best_word_char_4)
        if best_word_char_4 in possible_char_2_list:
            possible_char_2_list.remove(best_word_char_4)
        if best_word_char_4 in possible_char_3_list:
            possible_char_3_list.remove(best_word_char_4)
        if best_word_char_4 in possible_char_4_list:
            possible_char_4_list.remove(best_word_char_4)
        if best_word_char_4 in possible_char_5_list:
            possible_char_5_list.remove(best_word_char_4)
    if word_4_char_4_data == best_word_char_4:
        if best_word_char_4 in possible_char_4_list:
            possible_char_4_list.remove(best_word_char_4)
        if best_word_char_4 not in known_letters_list:
            known_letters_list.append(best_word_char_4)
    if word_4_char_4_data == 'gr':
        possible_char_4_list.clear()
        possible_char_4_list.append(best_word_char_4)
        if best_word_char_4 not in known_letters_list:
            known_letters_list.append(best_word_char_4)

    # Eliminate letter possibilites based on the user's inputted data
    if word_4_char_5_data == 'g':
        if best_word_char_5 in possible_char_1_list:
            possible_char_1_list.remove(best_word_char_5)
        if best_word_char_5 in possible_char_2_list:
            possible_char_2_list.remove(best_word_char_5)
        if best_word_char_5 in possible_char_3_list:
            possible_char_3_list.remove(best_word_char_5)
        if best_word_char_5 in possible_char_4_list:
            possible_char_4_list.remove(best_word_char_5)
        if best_word_char_5 in possible_char_5_list:
            possible_char_5_list.remove(best_word_char_5)
    if word_4_char_5_data == 'y':
        if best_word_char_5 in possible_char_5_list:
            possible_char_5_list.remove(best_word_char_5)
        if best_word_char_5 not in known_letters_list:
            known_letters_list.append(best_word_char_5)
    if word_4_char_5_data == 'gr':
        possible_char_5_list.clear()
        possible_char_5_list.append(best_word_char_5)
        if best_word_char_5 not in known_letters_list:
            known_letters_list.append(best_word_char_5)
    
    # Remove impossible words
    remove_unremoved_words(guess_number=4)


# Define a function to determine the best fifth word that the user should guess
def grab_fifth_word():
    global best_word_char_1,best_word_char_2,best_word_char_3,best_word_char_4,best_word_char_5
    # Define variables to track word sorting
    best_word = ['',0]
    current_score = 0

    # Sort each word based on how many characters it has in that haven't been guess yet
    for word in original_five_letter_word_list:
        if word[0] in unguessed_letters_list:
            current_score += 1
        if word[1] in unguessed_letters_list:
            current_score += 1
        if word[2] in unguessed_letters_list:
            current_score += 1
        if word[3] in unguessed_letters_list:
            current_score += 1
        if word[4] in unguessed_letters_list:
            current_score += 1
        if current_score > best_word[1]:
            best_word.clear()
            best_word.append(word)
            best_word.append(current_score)
        current_score = 0

    # Extract the best word from the sorting algorithm
    if best_word[1] > 0:
        best_word = best_word[0]
    else:
        print("No more unused characters, random word from possible words chosen.")
        if len(five_letter_words_list) == 0:
            print("Sorry there are no possible word combinations with the data you entered")
            quit()
        else:
            best_word = rand.choice(five_letter_words_list)

    # Split up the best word into 5 variables, each containing one of its characters
    best_word_char_1 = best_word[0]
    if best_word_char_1 in unguessed_letters_list:
        unguessed_letters_list.remove(best_word_char_1)
    best_word_char_2 = best_word[1]
    if best_word_char_2 in unguessed_letters_list:
        unguessed_letters_list.remove(best_word_char_2)
    best_word_char_3 = best_word[2]
    if best_word_char_3 in unguessed_letters_list:
        unguessed_letters_list.remove(best_word_char_3)
    best_word_char_4 = best_word[3]
    if best_word_char_4 in unguessed_letters_list:
        unguessed_letters_list.remove(best_word_char_4)
    best_word_char_5 = best_word[4]
    if best_word_char_5 in unguessed_letters_list:
        unguessed_letters_list.remove(best_word_char_5)


# Define a function to remove impossible words after the fifth guess
def remove_fifth_guess_words():
    grab_fifth_word()

    # Globalize data variables that will be used in other modules
    global word_5_char_1_data,word_5_char_2_data,word_5_char_3_data,word_5_char_4_data,word_5_char_5_data

    # Tell the user what the first word they should enter into wordle
    print("Enter the word", best_word_char_1+best_word_char_2+best_word_char_3+best_word_char_4+best_word_char_5, "as  your fourth guess.")
    print("\nPlease enter the corresponding data for each letter below:")

    # Get the resulting data of the first word's characters and don't let users enter bad inputs
    while True:
        word_5_char_1_data = str(input(best_word_char_1 + ": "))
        if word_5_char_1_data == 'g' or word_5_char_1_data == 'y' or word_5_char_1_data == 'gr':
            break
    while True:
        word_5_char_2_data = str(input(best_word_char_2 + ": "))
        if word_5_char_2_data == 'g' or word_5_char_2_data == 'y' or word_5_char_2_data == 'gr':
            break
    while True:
        word_5_char_3_data = str(input(best_word_char_3 + ": "))
        if word_5_char_3_data == 'g' or word_5_char_3_data == 'y' or word_5_char_3_data == 'gr':
            break
    while True:
        word_5_char_4_data = str(input(best_word_char_4 + ": "))
        if word_5_char_4_data == 'g' or word_5_char_4_data == 'y' or word_5_char_4_data == 'gr':
            break
    while True:
        word_5_char_5_data = str(input(best_word_char_5 + ": "))
        if word_5_char_5_data == 'g' or word_5_char_5_data == 'y' or word_5_char_5_data == 'gr':
            break
    
    # Output a mesage to the user that their data is being processed
    print("processing...")
    
    # Create globalized lists that contain the possible letters a specific character in the word can be
    global possible_char_1_list,possible_char_2_list,possible_char_3_list,possible_char_4_list,possible_char_5_list

    # Eliminate letter possibilites based on the user's inputted data
    if word_5_char_1_data == 'g':
        if best_word_char_1 in possible_char_1_list:
            possible_char_1_list.remove(best_word_char_1)
        if best_word_char_1 in possible_char_2_list:
            possible_char_2_list.remove(best_word_char_1)
        if best_word_char_1 in possible_char_3_list:
            possible_char_3_list.remove(best_word_char_1)
        if best_word_char_1 in possible_char_4_list:
            possible_char_4_list.remove(best_word_char_1)
        if best_word_char_1 in possible_char_5_list:
            possible_char_5_list.remove(best_word_char_1)
    if word_5_char_1_data == 'y':
        if best_word_char_1 in possible_char_1_list:
            possible_char_1_list.remove(best_word_char_1)
        if best_word_char_1 not in known_letters_list:
            known_letters_list.append(best_word_char_1)
    if word_5_char_1_data == 'gr':
        possible_char_1_list.clear()
        possible_char_1_list.append(best_word_char_1)
        if best_word_char_1 not in known_letters_list:
            known_letters_list.append(best_word_char_1)
    
    # Eliminate letter possibilites based on the user's inputted data
    if word_5_char_2_data == 'g':
        if best_word_char_2 in possible_char_1_list:
            possible_char_1_list.remove(best_word_char_2)
        if best_word_char_2 in possible_char_2_list:
            possible_char_2_list.remove(best_word_char_2)
        if best_word_char_2 in possible_char_3_list:
            possible_char_3_list.remove(best_word_char_2)
        if best_word_char_2 in possible_char_4_list:
            possible_char_4_list.remove(best_word_char_2)
        if best_word_char_2 in possible_char_5_list:
            possible_char_5_list.remove(best_word_char_2)
    if word_5_char_2_data == 'y':
        if best_word_char_2 in possible_char_2_list:
            possible_char_2_list.remove(best_word_char_2)
        if best_word_char_2 not in known_letters_list:
            known_letters_list.append(best_word_char_2)
    if word_5_char_2_data == 'gr':
        possible_char_2_list.clear()
        possible_char_2_list.append(best_word_char_2)
        if best_word_char_2 not in known_letters_list:
            known_letters_list.append(best_word_char_2)

    # Eliminate letter possibilites based on the user's inputted data
    if word_5_char_3_data == 'g':
        if best_word_char_3 in possible_char_1_list:
            possible_char_1_list.remove(best_word_char_3)
        if best_word_char_3 in possible_char_2_list:
            possible_char_2_list.remove(best_word_char_3)
        if best_word_char_3 in possible_char_3_list:
            possible_char_3_list.remove(best_word_char_3)
        if best_word_char_3 in possible_char_4_list:
            possible_char_4_list.remove(best_word_char_3)
        if best_word_char_3 in possible_char_5_list:
            possible_char_5_list.remove(best_word_char_3)
    if word_5_char_3_data == 'y':
        if best_word_char_3 in possible_char_3_list:
            possible_char_3_list.remove(best_word_char_3)
        if best_word_char_3 not in known_letters_list:
            known_letters_list.append(best_word_char_3)
    if word_5_char_3_data == 'gr':
        possible_char_3_list.clear()
        possible_char_3_list.append(best_word_char_3)
        if best_word_char_3 not in known_letters_list:
            known_letters_list.append(best_word_char_3)

    # Eliminate letter possibilites based on the user's inputted data
    if word_5_char_4_data == 'g':
        if best_word_char_4 in possible_char_1_list:
            possible_char_1_list.remove(best_word_char_4)
        if best_word_char_4 in possible_char_2_list:
            possible_char_2_list.remove(best_word_char_4)
        if best_word_char_4 in possible_char_3_list:
            possible_char_3_list.remove(best_word_char_4)
        if best_word_char_4 in possible_char_4_list:
            possible_char_4_list.remove(best_word_char_4)
        if best_word_char_4 in possible_char_5_list:
            possible_char_5_list.remove(best_word_char_4)
    if word_5_char_4_data == best_word_char_4:
        if best_word_char_4 in possible_char_4_list:
            possible_char_4_list.remove(best_word_char_4)
        if best_word_char_4 not in known_letters_list:
            known_letters_list.append(best_word_char_4)
    if word_5_char_4_data == 'gr':
        possible_char_4_list.clear()
        possible_char_4_list.append(best_word_char_4)
        if best_word_char_4 not in known_letters_list:
            known_letters_list.append(best_word_char_4)

    # Eliminate letter possibilites based on the user's inputted data
    if word_5_char_5_data == 'g':
        if best_word_char_5 in possible_char_1_list:
            possible_char_1_list.remove(best_word_char_5)
        if best_word_char_5 in possible_char_2_list:
            possible_char_2_list.remove(best_word_char_5)
        if best_word_char_5 in possible_char_3_list:
            possible_char_3_list.remove(best_word_char_5)
        if best_word_char_5 in possible_char_4_list:
            possible_char_4_list.remove(best_word_char_5)
        if best_word_char_5 in possible_char_5_list:
            possible_char_5_list.remove(best_word_char_5)
    if word_5_char_5_data == 'y':
        if best_word_char_5 in possible_char_5_list:
            possible_char_5_list.remove(best_word_char_5)
        if best_word_char_5 not in known_letters_list:
            known_letters_list.append(best_word_char_5)
    if word_5_char_5_data == 'gr':
        possible_char_5_list.clear()
        possible_char_5_list.append(best_word_char_5)
        if best_word_char_5 not in known_letters_list:
            known_letters_list.append(best_word_char_5)
    
    # Remove impossible words
    remove_unremoved_words(guess_number=5)

#####-Processing-#####
# Remove eliminated words from the possible words list after the first 2 guesses using preset words
remove_first_guess_words()
print(len(five_letter_words_list))
remove_second_guess_words()
print(len(five_letter_words_list))

# Remove eliminated words from the possible words list after the third guesses using an algorithmicly chosen word
remove_third_guess_words()
print(len(five_letter_words_list))

# Remove elimiated words from the possibel words list after the fourth guess using an algorithmically chosen word
remove_fourth_guess_words()
print(len(five_letter_words_list))
print(five_letter_words_list)

remove_fifth_guess_words()
print(known_letters_list)
'''
