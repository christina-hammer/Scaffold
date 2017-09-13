#Christina Hammer
#Last Edit: 09/13/2017

import nltk
import string

import sys

from Scaffold import *
from ScaffoldMaker import *
from helper_functions import *


if __name__ == "__main__":
    in_file_name = input('Please enter the name of the text file:')
    phrase_strings = open_and_split_by_phrase(in_file_name)
    
    out_file_name = input('Please the name of your Scaffold file:')
    
    scaffold_maker = ScaffoldMaker()
    
    #keywords is a global dic from helper_functions.py
    if KEYWORDS == None:
        load_keywords()    
        
    #takes in a list of strings (where each string is a phrase in the article)
    scaffold = scaffold_maker.create_scaffold(phrase_strings)    
    
    write_to_output_file(out_file_name, scaffold)
    
    
    
