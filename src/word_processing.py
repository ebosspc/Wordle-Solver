# Define a function to collect the corresponding data for the first word entered
def get_first_word_data():
    # Globalize data variables that will be used in other modules
    global word_1_char_1_data,word_1_char_2_data,word_1_char_3_data,word_1_char_4_data,word_1_char_5_data

    # Tell the user what the first word they should enter into wordle
    print("Enter the word Adieu as the your first guess.")
    print("\nPlease enter the corresponding data for each letter below:")

    # Get the resulting data of the first word's first character and don't let users enter bad inputs
    continue_with_loop = 0
    while continue_with_loop == 0:
        word_1_char_1_data = str(input("A: "))
        if word_1_char_1_data == 'g' or word_1_char_1_data == 'y' or word_1_char_1_data == 'gr':
            continue_with_loop = 1

    # Get the resulting data of the first word's second character and don't let users enter bad inputs
    continue_with_loop = 0
    while continue_with_loop == 0:
        word_1_char_2_data = str(input("D: "))
        if word_1_char_2_data == 'g' or word_1_char_2_data == 'y' or word_1_char_2_data == 'gr':
            continue_with_loop = 1

    # Get the resulting data of the first word's third character and don't let users enter bad inputs
    continue_with_loop = 0
    while continue_with_loop == 0:
        word_1_char_3_data = str(input("I: "))
        if word_1_char_3_data == 'g' or word_1_char_3_data == 'y' or word_1_char_3_data == 'gr':
            continue_with_loop = 1

    # Get the resulting data of the first word's fourth character and don't let users enter bad inputs
    continue_with_loop = 0
    while continue_with_loop == 0:
        word_1_char_4_data = str(input("E: "))
        if word_1_char_4_data == 'g' or word_1_char_4_data == 'y' or word_1_char_4_data == 'gr':
            continue_with_loop = 1

    # Get the resulting data of the first word's fifth character and don't let users enter bad inputs
    continue_with_loop = 0
    while continue_with_loop == 0:
        word_1_char_5_data = str(input("U: "))
        if word_1_char_5_data == 'g' or word_1_char_5_data == 'y' or word_1_char_5_data == 'gr':
            continue_with_loop = 1


# Define a function to process the first word data
def process_first_word_data():
    # Out put a mesage to the user that their data is being processed
    print("processing...")
    
    # Create globalized lists that contain the possible letters a specific character in the word can be
    global possible_char_1_list,possible_char_2_list,possible_char_3_list,possible_char_4_list,possible_char_5_list
    possible_char_1_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
                            ,'n','o','p','q','r','s','t','u','v','w','x','y','z']
    possible_char_2_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
                            ,'n','o','p','q','r','s','t','u','v','w','x','y','z']
    possible_char_3_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
                            ,'n','o','p','q','r','s','t','u','v','w','x','y','z']
    possible_char_4_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
                            ,'n','o','p','q','r','s','t','u','v','w','x','y','z']
    possible_char_5_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
                            ,'n','o','p','q','r','s','t','u','v','w','x','y','z']

    # Eliminate letter possibilites based on the user's inputted data
    if word_1_char_1_data == 'g':
        possible_char_1_list.remove('a')
        possible_char_2_list.remove('a')
        possible_char_3_list.remove('a')
        possible_char_4_list.remove('a')
        possible_char_5_list.remove('a')
    if word_1_char_1_data == 'y':
        possible_char_1_list.remove('a')
    if word_1_char_1_data == 'gr':
        possible_char_1_list.clear()
        possible_char_1_list.append('a')
    
    # Eliminate letter possibilites based on the user's inputted data
    if word_1_char_2_data == 'g':
        possible_char_1_list.remove('d')
        possible_char_2_list.remove('d')
        possible_char_3_list.remove('d')
        possible_char_4_list.remove('d')
        possible_char_5_list.remove('d')
    if word_1_char_2_data == 'y':
        possible_char_2_list.remove('d')
    if word_1_char_2_data == 'gr':
        possible_char_2_list.clear()
        possible_char_2_list.append('d')

    # Eliminate letter possibilites based on the user's inputted data
    if word_1_char_3_data == 'g':
        possible_char_1_list.remove('i')
        possible_char_2_list.remove('i')
        possible_char_3_list.remove('i')
        possible_char_4_list.remove('i')
        possible_char_5_list.remove('i')
    if word_1_char_3_data == 'y':
        possible_char_3_list.remove('i')
    if word_1_char_3_data == 'gr':
        possible_char_3_list.clear()
        possible_char_3_list.append('i')

    # Eliminate letter possibilites based on the user's inputted data
    if word_1_char_4_data == 'g':
        possible_char_1_list.remove('e')
        possible_char_2_list.remove('e')
        possible_char_3_list.remove('e')
        possible_char_4_list.remove('e')
        possible_char_5_list.remove('e')
    if word_1_char_4_data == 'y':
        possible_char_4_list.remove('e')
    if word_1_char_4_data == 'gr':
        possible_char_4_list.clear()
        possible_char_4_list.append('e')

    # Eliminate letter possibilites based on the user's inputted data
    if word_1_char_5_data == 'g':
        possible_char_1_list.remove('u')
        possible_char_2_list.remove('u')
        possible_char_3_list.remove('u')
        possible_char_4_list.remove('u')
        possible_char_5_list.remove('u')
    if word_1_char_5_data == 'y':
        possible_char_5_list.remove('u')
    if word_1_char_5_data == 'gr':
        possible_char_5_list.clear()
        possible_char_5_list.append('u')


# Define a function to collect the corresponding data for the first word entered
def get_second_word_data():
    # Globalize data variables that will be used in other modules
    global word_2_char_1_data,word_2_char_2_data,word_2_char_3_data,word_2_char_4_data,word_2_char_5_data

    # Tell the user what the first word they should enter into wordle
    print("Enter the word Cloys as the your second guess.")
    print("\nPlease enter the corresponding data for each letter below:")

    # Get the resulting data of the first word's first character and don't let users enter bad inputs
    continue_with_loop = 0
    while continue_with_loop == 0:
        word_2_char_1_data = str(input("C: "))
        if word_2_char_1_data == 'g' or word_2_char_1_data == 'y' or word_2_char_1_data == 'gr':
            continue_with_loop = 1

    # Get the resulting data of the first word's second character and don't let users enter bad inputs
    continue_with_loop = 0
    while continue_with_loop == 0:
        word_2_char_2_data = str(input("L: "))
        if word_2_char_2_data == 'g' or word_2_char_2_data == 'y' or word_2_char_2_data == 'gr':
            continue_with_loop = 1

    # Get the resulting data of the first word's third character and don't let users enter bad inputs
    continue_with_loop = 0
    while continue_with_loop == 0:
        word_2_char_3_data = str(input("O: "))
        if word_2_char_3_data == 'g' or word_2_char_3_data == 'y' or word_2_char_3_data == 'gr':
            continue_with_loop = 1

    # Get the resulting data of the first word's fourth character and don't let users enter bad inputs
    continue_with_loop = 0
    while continue_with_loop == 0:
        word_2_char_4_data = str(input("Y: "))
        if word_2_char_4_data == 'g' or word_2_char_4_data == 'y' or word_2_char_4_data == 'gr':
            continue_with_loop = 1

    # Get the resulting data of the first word's fifth character and don't let users enter bad inputs
    continue_with_loop = 0
    while continue_with_loop == 0:
        word_2_char_5_data = str(input("S: "))
        if word_2_char_5_data == 'g' or word_2_char_5_data == 'y' or word_2_char_5_data == 'gr':
            continue_with_loop = 1


# Define a function to process the second word data
def process_second_word_data():
    # Out put a mesage to the user that their data is being processed
    print("processing...")
    
    # Create globalized lists that contain the possible letters a specific character in the word can be
    global possible_char_1_list,possible_char_2_list,possible_char_3_list,possible_char_4_list,possible_char_5_list

    # Eliminate letter possibilites based on the user's inputted data
    if word_2_char_1_data == 'g':
        if 'c' in possible_char_1_list:
            possible_char_1_list.remove('c')
        if 'c' in possible_char_2_list:
            possible_char_2_list.remove('c')
        if 'c' in possible_char_3_list:
            possible_char_3_list.remove('c')
        if 'c' in possible_char_4_list:
            possible_char_4_list.remove('c')
        if 'c' in possible_char_5_list:
            possible_char_5_list.remove('c')
    if word_2_char_1_data == 'y':
        if 'c' in possible_char_1_list:
            possible_char_1_list.remove('c')
    if word_2_char_1_data == 'gr':
        possible_char_1_list.clear()
        possible_char_1_list.append('c')
    
    # Eliminate letter possibilites based on the user's inputted data
    if word_2_char_2_data == 'g':
        if 'l' in possible_char_1_list:
            possible_char_1_list.remove('l')
        if 'l' in possible_char_2_list:
            possible_char_2_list.remove('l')
        if 'l' in possible_char_3_list:
            possible_char_3_list.remove('l')
        if 'l' in possible_char_4_list:
            possible_char_4_list.remove('l')
        if 'l' in possible_char_5_list:
            possible_char_5_list.remove('l')
    if word_2_char_2_data == 'y':
        if 'l' in possible_char_2_list:
            possible_char_2_list.remove('l')
    if word_2_char_2_data == 'gr':
        possible_char_2_list.clear()
        possible_char_2_list.append('l')

    # Eliminate letter possibilites based on the user's inputted data
    if word_2_char_3_data == 'g':
        possible_char_1_list.remove('o')
        possible_char_2_list.remove('o')
        possible_char_3_list.remove('o')
        possible_char_4_list.remove('o')
        possible_char_5_list.remove('o')
    if word_2_char_3_data == 'y':
        possible_char_3_list.remove('o')
    if word_2_char_3_data == 'gr':
        possible_char_3_list.clear()
        possible_char_3_list.append('o')

    # Eliminate letter possibilites based on the user's inputted data
    if word_2_char_4_data == 'g':
        possible_char_1_list.remove('y')
        possible_char_2_list.remove('y')
        possible_char_3_list.remove('y')
        possible_char_4_list.remove('y')
        possible_char_5_list.remove('y')
    if word_2_char_4_data == 'y':
        possible_char_4_list.remove('y')
    if word_2_char_4_data == 'gr':
        possible_char_4_list.clear()
        possible_char_4_list.append('y')

    # Eliminate letter possibilites based on the user's inputted data
    if word_2_char_5_data == 'g':
        possible_char_1_list.remove('s')
        possible_char_2_list.remove('s')
        possible_char_3_list.remove('s')
        possible_char_4_list.remove('s')
        possible_char_5_list.remove('s')
    if word_2_char_5_data == 'y':
        possible_char_5_list.remove('s')
    if word_2_char_5_data == 'gr':
        possible_char_5_list.clear()
        possible_char_5_list.append('s')


# Define a function to determine the best thrid word that the user shoudl guess
def grab_third_word():
    global unguessed_letters_list,best_word_char_1,best_word_char_2,best_word_char_3,best_word_char_4,best_word_char_5
    unguessed_letters_list = ['b','f','g','h','j','k','m','n','p','q','r','t','v','w','x','y','z']

    # Define variables to track word sorting
    best_word = ['',0]
    current_score = 0

    # Sort each word based on how many characters it has in that haven't been guess yet
    for word in five_letter_words_list:
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
        best_word = rand.choice(five_letter_words_list)

    # Split up the best word into 5 variables, each containing one of its characters
    best_word_char_1 = best_word[0]
    best_word_char_2 = best_word[1]
    best_word_char_3 = best_word[2]
    best_word_char_4 = best_word[3]
    best_word_char_5 = best_word[4]