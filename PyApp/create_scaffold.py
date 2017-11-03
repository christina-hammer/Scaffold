#Christina Hammer
#Last Edit: 11/03/2017
#create_scaffold.py

#This collection of functions are used to perform necessary functions that aren't part of the main class structure of the program

import nltk
from Scaffold import *
from ScaffoldMaker import *


def create_scaffold(article_contents):
         
    phrase_strings = parse_and_tokenize_document_body(article_contents)    
    scaffold_maker = ScaffoldMaker()
        
    #takes in a list of strings (where each string is a phrase in the article)
    scaffold = scaffold_maker.create_scaffold(phrase_strings)
    config = set()
    return scaffold.display(config)

def parse_and_tokenize_document_body(input_article):
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    phrase_strings = sent_detector.tokenize(input_article.strip())    
    return phrase_strings

