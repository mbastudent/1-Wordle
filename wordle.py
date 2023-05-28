#!/usr/bin/env python
# coding: utf-8

# In[10]:


"""
Contains sets of English words from svnweb.freebsd.org/csrg/share/dict/. This is up to date with revision 61569 of their words list.

There are four sets in this package:

english_words_set: A set of English words containing both upper- and lower-case letters; with punctuation.
english_words_lower_set: A set of English words containing lower-case letters; with punctuation.
english_words_alpha_set: A set of English words containing both upper- and lower-case letters; with no punctuation.
english_words_lower_alpha_set: A set of English words containing lower-case letters; with no punctuation.
where the lower set is the same as the english_words_set with all upper-case letters converted to lower-case letters, and where the alpha set is the same as the english_words_set with all apostrophes (') removed. The lower_alpha set intuitively has both of the rules from the lower set and the alpha set applied.

You can use use these like you would any Python set:

>>> from english_words import english_words_set
>>> 'ghost' in english_words_set

"""
import random
from english_words import english_words_lower_alpha_set



# returns a random word from the list of all words
def random_word(words):
    upper = len(words)
    random_number = random.randint(1, upper)
    return words[random_number-1]
    

# checks if guessed word is even a word from a list
def is_real_word(guess_word, words_full_list):
    if guess_word in words_full_list:
        return True
    else:
        return False

    
# checks if guessed word has same length as THE word
def is_length_OK(guess_word, the_word):
    if len(guess_word) == len(the_word):
        return True
    else:
        return False

    
def check_guess(guess_word, the_word):
    #creates list of '_'s
    icons = []
    while len(icons) < len(the_word):
        icons.append('_')
        
    used_X = []
    used_O = []
    for index in range(len(guess_word)):
        occurance = the_word.count(guess_word[index])
        if guess_word[index] == the_word[index]:
            icons[index] = "X"
            used_X.append(guess_word[index])
        elif guess_word[index] in the_word:
            if guess_word[index] in used_X:
                icons[index] = "_"
            else:
                if guess_word[index] in used_O and occurance<2:
                    icons[index] = "_"
                else:
                    icons[index] = "O"
                    used_O.append(guess_word[index])
    return "".join(icons)


def next_guess(words_full_list, the_word):
    validity = False
    while not validity:
        guess_word = input("Enter your guess: ").lower()
        validity = is_real_word(guess_word, words_full_list) and is_length_OK(guess_word, the_word)
    return guess_word
    

def play():
    words_full_list = list(english_words_lower_alpha_set)
    the_word = random_word(words_full_list)
    print("This is a", len(the_word), "letter word")
       
    count = 1
    while count <= 6:
        print("Attempt no: ",count)
        guess_word = next_guess(words_full_list, the_word)
        print(guess_word)
        icons = check_guess(guess_word, the_word)
        print(icons)
        
        if guess_word == the_word:
            print("You won!")
            return True
            
        count += 1
    
    print("You lost!")
    print("The word was", the_word)
    return False
    
    
play()


# In[ ]:




