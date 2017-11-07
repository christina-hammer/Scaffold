#Christina Hammer
#Last Edit: 11/06/2017
#create_scaffold.py

#This collection of functions are used to perform necessary functions that aren't part of the main class structure of the program

import nltk
from Scaffold import *
from ScaffoldMaker import *

def ascii_equiv(c):
    c_val = ord(c)
    replacements = {145:39, 146:39, 147:34, 148:34, 150:45, 151:45}
    if (c_val in replacements):
        return chr(replacements[c_val])
    #else:
    #write code to keep track of non-ascii characters that there aren't cases for already so they can be added
    return ""

def replace_non_ascii(string_):
    
    for c in string_:
        if ord(c) > 127:
            string_ = string_.replace(c, ascii_equiv(c))
    return string_


def create_scaffold(article_contents):
        
    phrase_strings = parse_and_tokenize_document_body(article_contents) 
    
    scaffold_maker = ScaffoldMaker()
        
    #takes in a list of strings (where each string is a phrase in the article)
    scaffold = scaffold_maker.create_scaffold(phrase_strings)
    config = set()
    return scaffold.display(config)

def parse_and_tokenize_document_body(input_article):
    input_article = replace_non_ascii(input_article)
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    phrase_strings = sent_detector.tokenize(input_article.strip())
          
    return phrase_strings

