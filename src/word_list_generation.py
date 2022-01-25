# Define a functionto generate a list of words and characters from the database of English words
def generate_words_list():
    # Open the word database and a corresponding list to store words
    global master_words_list
    master_words_list = []
    words_database_file = open("words_database.txt", 'r')

    # Add each word to the words list, broken up into a list of characters with the endline removed
    for line in words_database_file:
        individual_word = line.strip() # Remove the endline
        master_words_list.append(list(individual_word)) # Break up word into list of characters
    words_database_file.close()


# Define a function to generate a list of 5 letter words
def get_5_letter_words():
    # Creat e list of five letter words
    global five_letter_words_list
    five_letter_words_list = []

    # Add 5 letter words from the master words list to the 5 letter word list
    generate_words_list()
    for word in master_words_list:
        if len(word) == 5:
            five_letter_words_list.append(word)
