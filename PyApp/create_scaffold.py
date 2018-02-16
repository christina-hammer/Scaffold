#Christina Hammer
#Last Edit: 12/07/2017
#create_scaffold.py

#This collection of functions are used to perform necessary functions that aren't part of the main class structure of the program

import nltk
from Scaffold import *
from ScaffoldMaker import *


def clean_non_english_punc(string_):
    replacements = {145:39, 146:39, 147:34, 148:34, 150:45, 151:45, 8217: 39, 8217:39, 8220:34, 8221:34, 8211:45, 8212:45, 91:40, 93:41}
    removals = {42, 64, 92, 94, 95, 126}
    for s in string_:
        if ord(s) in replacements:            
            string_ = string_.replace(s, chr(replacements[ord(s)]))
        elif ord(s) in removals:
            string_ = string_.replace(s, "")    
    
    return string_


def create_scaffold(article_contents):
    #print("before parse_and_tokenize")  
    phrase_strings = parse_and_tokenize_document_body(article_contents) 
    #print("before scaffold_maker")
    scaffold_maker = ScaffoldMaker()
    #print("before create_scaffold")   
    #takes in a list of strings (where each string is a phrase in the article)
    scaffold = scaffold_maker.create_scaffold(phrase_strings)
    #print("before return in create_scaffold")
    return scaffold

def parse_and_tokenize_document_body(input_article):
    #print("before clean_non_english_punc")
    input_article = clean_non_english_punc(input_article)
    #print("before load download") 

    # try:
    #     print("before load pickle") 
    #     nltk.data.load('tokenizers/punkt/english.pickle')        
    # except ValueError as e:
    #     print(str(e))
    #     print("what the actual fuck")
    #nltk.download('punkt')
    
    #print("before load pickle ") 

    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

    #print("before tokenize")
    phrase_strings = sent_detector.tokenize(input_article.strip())
    #print("before return in parse_and_tokenize")
    return phrase_strings

