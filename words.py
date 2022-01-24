# Define a functionto generate a list of words and characters from the database of English words
def generate_words_list():
    # Open the word database and a corresponding list to store words
    global master_words_list
    master_words_list = []
    words_database_file = open("samplewords.txt", 'r')

    # Add each word to the words list, broken up into a list of characters with the endline removed
    for line in words_database_file:
        individual_word = line.strip() # Remove the endline
        master_words_list.append(list(individual_word)) # Break up word into list of characters
    words_database_file.close()
    print("bop")
    return master_words_list