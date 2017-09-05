#Christina Hammer
#Last Edit: 09/05/2017
#helper_functions.py

from Phrase import *
from Token import *

KEYWORDS = None

##credit to:
##https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float
##works on decimals, ints
def is_digit_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False 
    
#this will actually load a json and save it as a dictionay. just populating a small dictionary right now as placeholder
def load_keywords():
    # example dictionary: KEYWORDS = {"a.m.": "DT", "p.m.": "DT"}
    KEYWORDS = {}
    return

def close_keywords():
    #close json
    KEYWORDS = None
    return
    
def check_if_keyword(text):
    if KEYWORDS == None:
        load_keywords()
    return 
    
#def is_text_number(s):
    #s.lower()
    ##need to add more cases and also deal with hyphen situations thirty-three etc.
    #num_dic = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred", "million", "billion", "trillion"}
    
    #if s in num_dic:
        #return True
    #else:
        #return False
    
##the only times that should be replaced with words are the ones below:
#def is_time_word(text):
    #return text in {"midnight", "noon"}


#small sample of common prepositions, articles, and coordinating conjunctions
#to deal with keeping multi-word names like "University of California" as one item
#likely portal to hell for false positives. We'll see.
def common_connector(word):
    return word in {'of','the','in','and', 'for'}


def connected_proper_nouns(phrase, first_pn, second_pn):
    for i in range(first_pn+1, second_pn):
        if not(common_connector(phrase[i])):
            return False
    return True

def string_to_phrase(phrase_string):
        phrase = Phrase()
        tokenized_phrase = phrase_string.split()
        
        for i in range(0, len(tokenized_phrase)):
            t = Token(tokenized_phrase[i], i)
            phrase.add_token(t)
            
        return phrase