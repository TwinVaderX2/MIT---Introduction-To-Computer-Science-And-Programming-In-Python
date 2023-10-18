# Problem Set 4B
# Name: Phillip van Staden


import os
import random

# ================== CREATE RELATIVE PATH FOR FILE ================
# relative path for words.txt file
WORDLIST_FILENAME = "words.txt"
absolute_path = os.path.dirname(__file__)
relative_path = "../resources/"+ WORDLIST_FILENAME
words_full_path = os.path.join(absolute_path,relative_path)

# relative path for story.txt
STORY_FILENAME = 'story.txt'
relative_path = "../resources/" + STORY_FILENAME
story_full_path = os.path.join(absolute_path,relative_path)

### HELPER CODE ###
def load_words(words_full_path):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(words_full_path, 'r')
    # word_list: list of strings
    word_list = []
    for line in inFile:
        word_list.extend([word.lower() for word in line.split(' ')])
    print("  ", len(word_list), "words loaded.")
    return word_list

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string(story_full_path):
    """
    Returns: a story in encrypted text.
    """
    f = open(story_full_path, "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

class Message():
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(words_full_path)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text
    
    def __str__(self):
        
        return f'The original message is: {self.message_text}'

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        valid_words_copy = self.valid_words.copy()

        return valid_words_copy

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 

        Returns: None if incorrect input is detected.
        '''
        try:
            int(shift)

            if shift <= 26:
                alphabet = 'abcdefghijklmnopqrstuvwxyz'
                caps_alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

                # Create list of char in alphabet (including capital letters)
                alphabet_ls = [i for i in alphabet]
                caps_ls = [i for i in caps_alph]
                
                # Create new alphabet shifting letters (in alphabet) by 'shift'
                cipher_alph = alphabet[shift:]+alphabet[:shift]
                caps_cipher_alph = caps_alph[shift:]+caps_alph[:shift]
                
                # Create list of char in alphabet
                cipher_alph_ls = [i for i in cipher_alph]
                caps_cipher_alph_ls = [i for i in caps_cipher_alph]
                
                # Combine two list to create new cipher
                cipher_lower = dict(zip(alphabet_ls,cipher_alph_ls))
                cipher_caps = dict(zip(caps_ls,caps_cipher_alph_ls))

                # join two ciphers
                cipher = {**cipher_lower, **cipher_caps}
                
                return cipher
            
            else:
                print('Error, unable to create cipher.\nPlease enter a number between 0 and 26.')
                return None

        except TypeError:
            print("You have made an invalid input, unable to create cipher.")
            return None
        

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        cipher = self.build_shift_dict(shift)
        message_text_ls = [i for i in self.message_text]
        new_message_text = ''

        for idx in message_text_ls:
            if idx in cipher:
                new_message_text = new_message_text + cipher.get(idx)
            else:
                new_message_text = new_message_text + idx
        
        return new_message_text

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        self.message_text = text
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)
        

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        encryp_dict_copy = self.encryption_dict.copy()

        return encryp_dict_copy

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted
    
    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other
        attributes determined by shift.
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text # shouldn't this be message_text_encrypted??
        self.valid_words = load_words(words_full_path)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        # create dictionary for shift keys with default value: 0
        shift_dict = dict.fromkeys((i for i in range(1,27)),0)
        message_text_ls = [i for i in self.message_text]
        
        def build_decrypted_message(shift,message_text_ls):
            # get cipher
            cipher = self.build_shift_dict(shift)
            # decrypt using chiper
            new_message_text = ''

            for idx in message_text_ls:
                if idx in cipher:
                    new_message_text = new_message_text + list(cipher.keys())[list(cipher.values()).index(idx)]
                else:
                    new_message_text = new_message_text + idx
            
            return new_message_text

        # loop through (1 - 26) chiphers
        for i in range(26):
            
            new_message_text = build_decrypted_message(i,message_text_ls)
            # break up into seperate words
            sub_strings = new_message_text.strip('!.?').split(', ')
            count = 0
            # test each word (loop) if valid
            for j in sub_strings:
                # if valid, increase count
                if j.lower() in self.valid_words:
                    count += 1
            # store count (relative to shift key)

            shift_dict[i] = count

        # determine shift_key with max value (if more than one, return all)
        max_keys = [key for key, value in shift_dict.items() if value == max(shift_dict.values())]
        
        # if more than 1 shift_key
        if len(max_keys) > 1:
            # choose random element from list
            random_shift = random.choice(max_keys)
            # build tuple that displays the shift_key and decrypted message
            best_cipher = (random_shift,build_decrypted_message(random_shift,message_text_ls))
            return best_cipher
        else:
            # build tuple that displays the shift_key and decrypted message
            best_cipher = (max_keys[0],build_decrypted_message(max_keys[0],message_text_ls))
            return best_cipher

if __name__ == '__main__':

    story = get_story_string(story_full_path)
    cipher_text = CiphertextMessage(story)
    print('The original encoded message: ',cipher_text,'\nThe decoded message is: ',cipher_text.decrypt_message())

#    #Example test case (PlaintextMessage)
#    plaintext = PlaintextMessage('hello', 2)
#    print('Expected Output: jgnnq')
#    print('Actual Output:', plaintext.get_message_text_encrypted())

#    #Example test case (CiphertextMessage)
#    ciphertext = CiphertextMessage('jgnnq')
#    print('Expected Output:', (2, 'hello'))
#    print('Actual Output:', ciphertext.decrypt_message())
    

