#Christina Hammer
#Last Edit: 8/30/2017

import nltk
import string
import nltk.tag
from nltk import tokenize
from nltk import pos_tag
import sys

from Scaffold import *
from ScaffoldMaker import *


def open_and_split_by_phrase(article_text_file_name):
    
    try:
        f = open(article_text_file_name)
    except IOError:
        sys.exit("Cannot Open File")
    
    try:    
        input_article = f.read()
    except IOError:
        sys.exit("Cannot Read File")
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    phrase_strings = sent_detector.tokenize(input_article.strip())
    
    ##list of strings
    return phrase_strings

def write_output_to_file(of_name, scaffold):
    
    outf = open(of_name, 'w')
    scaffold_output = scaffold.display()
        
    outf.write(scaffold)        
    outf.close() 
        
    return
    
if __name__ == "__main__":
    title = input('Please enter the name of the text file:')
    phrase_strings = open_and_split_by_phrase(title)
    
    of_name = input('Please the name of your Scaffold file:')
    
    scaffold_maker = ScaffoldMaker()
    #takes in a list of strings (where each string is a phrase in the article)
    scaffold = scaffold_maker.createScaffold(phrase_strings)    
    
    write_to_output_file(of_name, scaffold)
    
    
    