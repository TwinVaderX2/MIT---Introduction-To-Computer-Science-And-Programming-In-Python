# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import os

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    source = os.path.abspath('../resources/words.txt')
    inFile = open(source, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    # print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    
    # split secret word into separate letters
    letters_in_secret_word = [x for x in secret_word]
    is_in_word = []

    # test if letter in the secret word appears in the list of guessed letters
    # add true to list if found, false if not found
    for idx in letters_in_secret_word:
        if idx in letters_guessed:
            is_in_word.append(True)
        else:
            is_in_word.append(False)

    # test if false is in list - indicates that a letter in secret word has not been guessed
    if False in is_in_word:
        word_is_guessed = False
    else:
        word_is_guessed = True

    return word_is_guessed

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # split secret word into separate letters
    letters_in_secret_word = [x for x in secret_word]

    # create new variable
    new_word = []
    guessed_word = ""

    # test letters_in_secret_word against letters guessed
    # if letters are a match, add letter to new word
    # if no match, add _ to new word
    for letter in letters_in_secret_word:
        if letter in letters_guessed:
            new_word.append(letter)
        else:
            new_word.append("_ ")
              

    guessed_word = guessed_word.join(new_word)
    
    return guessed_word

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters_available_list = []
    letters_available = ""

    # test if letter in alphabet appears in letters_guessed
    # if not found, add to list of available letters
    for letter in string.ascii_lowercase:
        if letter in letters_guessed:
            pass
        else:
            letters_available_list.append(letter)
    
    # convert list into string
    letters_available = letters_available.join(letters_available_list)

    return letters_available

def guess_word(secret_word,num_of_guesses):
    """
        Function request user input to guess the secret word. Uses functions: is_word_guessed, get_guessed_word and available_letters
        to determine if the secret word has been guessed and to provide the user with clues.

        Parameters:
        secret_word: STRING
                    The secret word that must be guessed by the user.

        num_of_guesses: INT
                    Number of guesses available 
        
        Output: NULL
    """
    # create varaibles
    letters_guessed = []
    count = 1

    # request user input (loop for number of guesses)
    while count <= num_of_guesses:
        print(f"You have {num_of_guesses-count+1} guesses left.")
        user_input = input("Please enter your guess:\n").lower()

        if len(user_input) == 1:  # check if user input is only one character
            
            if user_input.isalpha(): # check if user input is alpha character
                letters_guessed.append(user_input)
                if is_word_guessed(secret_word,letters_guessed): # call function to check if secret word is guessed
                    print("Congratulations, you have guess the secret word.")
                    print(get_guessed_word(secret_word,letters_guessed))
                    print(f"You scored: {(num_of_guesses-count)*len(secret_word)}")
                    break
                elif count == num_of_guesses:
                    print(f"Sorry, but you didn't manage to guess the word correctly.\n The secret word was: {secret_word} \n Please try again.")
                    break
                else:
                    print("You have guessed the following letters correctly: "+get_guessed_word(secret_word,letters_guessed))
                    print("You still have the following letters available to guess from: "+ get_available_letters(letters_guessed))
                    count += 1
            else:
                print("You've made an incorrect input.") # error message
        else:
            print("Please enter only one letter at a time.") # error message

def guess_with_hint(secret_word):
    '''
        Function loops throught the length of the secret_word and provides a hint once the user
        has 3 guesses left.

        Parameters:
        secret_word: STRING - secret word that the user must guess using input

        Return: NONE
    '''
    # create variables
    count = 0
    letters_guessed = []

    while count != len(secret_word):
        #display number of guesses left
        print(f'You have {len(secret_word)-count} guesses left.')
        user_guess = input("Please enter your guess:\n").lower()

        # test if the user has made only one character input
        if len(user_guess) > 1:
            print("Please enter only one character at a time.")

        elif len(user_guess) < 1:
            print("No input detected.")

        elif user_guess == "*":
            print("You have successfully entered the cheat code, I will now show you all the possible matches based on the letters guessed thus far.")
            my_word = get_guessed_word(secret_word,letters_guessed)
            show_possible_matches(my_word)

        else:
            # test if the user has made the correct input
            if user_guess.isalpha():
                count += 1
                letters_guessed.append(user_guess)

                if is_word_guessed(secret_word,letters_guessed): # call function to check if secret word is guessed
                        print("Congratulations, you have guess the secret word.")
                        print(get_guessed_word(secret_word,letters_guessed))
                        print(f"You scored: {(len(secret_word)-count)*len(secret_word)}")
                        break
                
                elif count == len(secret_word):
                    print(f"Sorry, but you didn't manage to guess the word correctly.\n The secret word was: {secret_word} \n Please try again.")
                    break

                elif (len(secret_word)-count) == 2:
                    my_word = get_guessed_word(secret_word,letters_guessed)
                    show_possible_matches(my_word)
                
                else:
                    print("You have guessed the following letters correctly: "+get_guessed_word(secret_word,letters_guessed))
                    print("You still have the following letters available to guess from: "+ get_available_letters(letters_guessed))
            
            else:
                print("You've made an incorrect input.") # error message


def hangman(secret_word):
    '''
    Starts up an interactive game of Hangman.
    
    * print welcome message

    * request user to select difficulty level

    * request user input to guess secret word

    Parameters:
    secret_word: string, the secret word to guess.
    
    Ouput: NULL
    '''
    welcome_message = """
                        Welcome and thank you for playing hangman

                        I have chosen a secret word that you must guess.

                        I will tell you how many letters are in the secret word.

                        You will be allowed to guess which letters appear the word.

                        After each guess, I will tell you if you've guessed the secret word.

                        If you haven't guessed the secret word, I will show you which letters you
                        have guessed.

                        If you do not guess the secret word before the end of the game, I WIN!
                      """
    
    difficulty_menu = """
                        You can select one of the following difficulty settings:
                        (b) Beginner level - Length of the word + 6 guesses
                        (i) Intermediate - Length of the word + 3 guesses
                        (e) Expert - Length of the word
                        (w) With hints - Length of the word + with a hint

                        (q) Quit - Exit Program

                        Please make your selection \n
                      """
    letters_guessed = []
    print(welcome_message)
    
    while True:
      user_input = input(difficulty_menu).lower()
      if user_input.isalpha():
        if user_input == 'b':
            print("You have selected beginner mode.")
            print("You must guess a word with: "+str(len(secret_word))+" letters. \nYou will have: " + str(len(secret_word)+6)+" guesses.")
            print(get_guessed_word(secret_word,letters_guessed))
            print("Let's begin.")
            guess_word(secret_word,(len(secret_word)+6))
            break
            
        elif user_input == 'i':
            print("You have selected intermediate mode.")
            print("You must guess a word with: "+str(len(secret_word))+" letters. \nYou will have: " + str(len(secret_word)+3)+" guesses.")
            print(get_guessed_word(secret_word,letters_guessed))
            print("Let's begin.")
            guess_word(secret_word,(len(secret_word)+3))
            break

        elif user_input == 'e':
            print("You have selected beginner mode.")
            print("You must guess a word with: "+str(len(secret_word))+" letters. \nYou will have: " + str(len(secret_word))+" guesses.")
            print(get_guessed_word(secret_word,letters_guessed))
            print("Let's begin.")
            guess_word(secret_word,(len(secret_word)))
            break

        elif user_input == 'w':
            print("You have selected Expert level with a hint.")
            print("You must guess a word with: "+str(len(secret_word))+" letters. \nYou will have: " + str(len(secret_word))+" guesses.\nI will give you one hint when you have 3 guesses left.")
            print(get_guessed_word(secret_word,letters_guessed))
            print("Let's begin.")
            guess_with_hint(secret_word)
            break

        elif user_input == 'q':
            print("Thank you for playing hangman. Please come again.")
            break
        
        else:
            print("You've made an invalid selection")
      else:
          print("You have made an invalid selection.")

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # set variables
    does_match = False
    my_word_length = len(my_word.strip(" "))
    other_word_length = len(other_word)
    # set variables
    is_match = False
    my_word_length = 0
    other_word_length = len(other_word)
    my_word_list = []
    other_word_list = []

    # split my_word into characters in list
    for idx in my_word:
        if idx != " ":
            my_word_list.append(idx.strip())

    # set length of my_word_length
    my_word_length = len(my_word_list)

    # split other_word into characters in list
    for idx in other_word:
        other_word_list.append(idx)

    # test if lenghts of two words are match
    if my_word_length == other_word_length:
        # test characters in each position of both words for match
        # set is_match to TRUE if positions match
        for idx in range(other_word_length):
            if my_word_list[idx] == other_word_list[idx] or my_word_list[idx] == "_":
                is_match = True
            # if match not found return false and break loop
            else:
                is_match = False
                break
    
    return is_match



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # load words into list
    wordlist = load_words()

    # create variables
    possible_words = []

    # cycle through list of words, test to see if word is a match, add to list of possible words
    for idx in wordlist:
        if match_with_gaps(my_word,idx):
            possible_words.append(idx)

    print(f"You have been able to correctly guess the following: {my_word}\nOne of the following words is your secret word:\n{possible_words}")



if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    # secret_word = 'apple'
    hangman(secret_word)
