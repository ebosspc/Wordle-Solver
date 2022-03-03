# Define a function to create a global variable that has the highest net frequency
def generate_highest_net_frequency_word():
    # Open the word database and add 5 letter words to a corresponding list
    five_letter_words_list_all_words = []
    words_database_file = open("Words_English.txt", 'r')
    for line in words_database_file:
        individual_word = line.strip() # Remove the endline character from each line before storing
        if len(individual_word) == 5:
            five_letter_words_list_all_words.append(individual_word) # Add 5 letter word to the list
    five_letter_word_list = five_letter_words_list_all_words

    # Generate frequency scores for all of the letters
    a_list = []
    b_list = []
    c_list = []
    d_list = []
    e_list = []
    f_list = []
    g_list = []
    h_list = []
    i_list = []
    j_list = []
    k_list = []
    l_list = []
    m_list = []
    n_list = []
    o_list = []
    p_list = []
    q_list = []
    r_list = []
    s_list = []
    t_list = []
    u_list = []
    v_list = []
    w_list = []
    x_list = []
    y_list = []
    z_list = []
    for word in five_letter_word_list:
        for char in word:
            if char == 'a':
                a_list.append(char)
            if char == 'b':
                b_list.append(char)
            if char == 'c':
                c_list.append(char)
            if char == 'd':
                d_list.append(char)
            if char == 'e':
                e_list.append(char)
            if char == 'f':
                f_list.append(char)
            if char == 'g':
                g_list.append(char)
            if char == 'h':
                h_list.append(char)
            if char == 'i':
                i_list.append(char)
            if char == 'j':
                j_list.append(char)
            if char == 'k':
                k_list.append(char)
            if char == 'l':
                l_list.append(char)
            if char == 'm':
                m_list.append(char)
            if char == 'n':
                n_list.append(char)
            if char == 'o':
                o_list.append(char)
            if char == 'p':
                p_list.append(char)
            if char == 'q':
                q_list.append(char)
            if char == 'r':
                r_list.append(char)
            if char == 's':
                s_list.append(char)
            if char == 't':
                t_list.append(char)
            if char == 'u':
                u_list.append(char)
            if char == 'v':
                v_list.append(char)
            if char == 'w':
                w_list.append(char)
            if char == 'x':
                x_list.append(char)
            if char == 'y':
                y_list.append(char)
            if char == 'z':
                z_list.append(char)
    a_score = round(((100*len(a_list))/15918),2)
    b_score = round(((100*len(b_list))/15918),2)
    c_score = round(((100*len(c_list))/15918),2)
    d_score = round(((100*len(d_list))/15918),2)
    e_score = round(((100*len(e_list))/15918),2)
    f_score = round(((100*len(f_list))/15918),2)
    g_score = round(((100*len(g_list))/15918),2)
    h_score = round(((100*len(h_list))/15918),2)
    i_score = round(((100*len(i_list))/15918),2)
    j_score = round(((100*len(j_list))/15918),2)
    k_score = round(((100*len(k_list))/15918),2)
    l_score = round(((100*len(l_list))/15918),2)
    m_score = round(((100*len(m_list))/15918),2)
    n_score = round(((100*len(n_list))/15918),2)
    o_score = round(((100*len(o_list))/15918),2)
    p_score = round(((100*len(p_list))/15918),2)
    q_score = round(((100*len(q_list))/15918),2)
    r_score = round(((100*len(r_list))/15918),2)
    s_score = round(((100*len(s_list))/15918),2)
    t_score = round(((100*len(t_list))/15918),2)
    u_score = round(((100*len(u_list))/15918),2)
    v_score = round(((100*len(v_list))/15918),2)
    w_score = round(((100*len(w_list))/15918),2)
    x_score = round(((100*len(x_list))/15918),2)
    y_score = round(((100*len(y_list))/15918),2)
    z_score = round(((100*len(z_list))/15918),2)

    # Sort through every word and find the one with the highest net frequency
    best_word = ['',0]
    optimal_word = []
    for word in five_letter_word_list:
        score = 0
        for char in word:
            if char == 'a':
                score += a_score
            if char == 'b':
                score += b_score
            if char == 'c':
                score += c_score
            if char == 'd':
                score += d_score
            if char == 'e':
                score += e_score
            if char == 'f':
                score += f_score
            if char == 'g':
                score += g_score
            if char == 'h':
                score += h_score
            if char == 'i':
                score += i_score
            if char == 'j':
                score += j_score
            if char == 'k':
                score += k_score
            if char == 'l':
                score += l_score
            if char == 'm':
                score += m_score
            if char == 'n':
                score += n_score
            if char == 'o':
                score += o_score
            if char == 'p':
                score += p_score
            if char == 'q':
                score += q_score
            if char == 'r':
                score += r_score
            if char == 's':
                score += s_score
            if char == 't':
                score += t_score
            if char == 'u':
                score += u_score
            if char == 'v':
                score += v_score
            if char == 'w':
                score += w_score
            if char == 'x':
                score += x_score
            if char == 'y':
                score += y_score
            if char == 'z':
                score += z_score
        if score > best_word[1]:
            optimal_word.clear()
            for char in word:
                optimal_word.append(char)
                if len(set(optimal_word)) == len(optimal_word): # Check if word has all unique letters
                    unique = 1
                else:
                    unique = 0
                    break
            if unique == 1:
                best_word.clear()
                best_word.append(word)
                best_word.append(score)
        score = 0
    global highest_net_frequency_word
    highest_net_frequency_word = best_word[0]
