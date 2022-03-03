# Define a function to generate lists with possible letters and unguessed letters
def generate_deduction_lists():
    # Create global lists with ungusessed letters and possibilites for each character
    global unguessed_letters_list, known_letters_list
    global possible_char_1_list,possible_char_2_list,possible_char_3_list,possible_char_4_list,possible_char_5_list
    unguessed_letters_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                            'n','o','p','q','r','s','t','u','v','w','x','y','z']
    possible_char_1_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                            'n','o','p','q','r','s','t','u','v','w','x','y','z']
    possible_char_2_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                            'n','o','p','q','r','s','t','u','v','w','x','y','z']
    possible_char_3_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                            'n','o','p','q','r','s','t','u','v','w','x','y','z']
    possible_char_4_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                            'n','o','p','q','r','s','t','u','v','w','x','y','z']
    possible_char_5_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                            'n','o','p','q','r','s','t','u','v','w','x','y','z']
    known_letters_list = []


# Define a function to generate a list of 5 letter words using every word in the English language
def get_5_letter_words_list_all_words():
    # Create a list to store 5 letter words
    global five_letter_words_list_all_words
    five_letter_words_list_all_words = []

    # Open the word database and add 5 letter words to a corresponding list
    words_database_file = open("Words_English.txt", 'r')
    for line in words_database_file:
        individual_word = line.strip() # Remove the endline character from each line before storing
        if len(individual_word) == 5:
            five_letter_words_list_all_words.append(individual_word) # Add 5 letter word to the list


# Define a function to generate a list of 5 letter words using the database of possible word inputs to wordle
def get_5_letter_words_list_all_inputs():
    # Create a list to store 5 letter words
    global five_letter_words_list_all_inputs
    five_letter_words_list_all_inputs = []

    # Open the word database and add 5 letter words to a corresponding list
    words_database_file = open("Words_Possible-Answers.txt", 'r')
    for line in words_database_file:
        individual_word = line.strip() # Remove the endline character from each line before storing
        if len(individual_word) == 5:
            five_letter_words_list_all_inputs.append(individual_word) # Add 5 letter word to the list


# Define a function to generate a list of 5 letter words using the database of all known answers to worlde puzzles
def get_5_letter_words_list_all_answers():
    # Define a function to generate a list of 5 letter words using the database of possible word inputs to wordle
    global five_letter_words_list_all_answers
    five_letter_words_list_all_answers = []

    # Open the word database and add 5 letter words to a corresponding list
    words_database_file = open("Words_Answers.txt", 'r')
    for line in words_database_file:
        individual_word = line.strip() # Remove the endline character from each line before storing
        if len(individual_word) == 5:
            five_letter_words_list_all_answers.append(individual_word) # Add 5 letter word to the list
