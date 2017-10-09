#Christina Hammer
#Last Edit: 10/08/2017
#helper_functions.py

import nltk
import json
from datetime import datetime
import re

def open_and_split_by_phrase(in_file):
    
    try:
        f = open(in_file)
    except IOError:
        sys.exit("Cannot Open File")
    try:    
        input_article = f.read()
    except IOError:
        sys.exit("Cannot Read File")
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    phrase_strings = sent_detector.tokenize(input_article.strip())
    
    #list of strings
    return phrase_strings

def write_to_output_file(scaffold):
    
    test_dt = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    of_name = str("scaffold" + test_dt + ".txt")
    
    outf = open("output/" + of_name, 'w')
    scaffold_output = scaffold.display()
    
    outf.write(scaffold_output)        
    outf.close() 
        
    return
  
def load_keywords():
    #write code to load JSON file into dictionary    
    keyword_json = open("keywords.json")
    keyword_string = keyword_json.read() 
    keywords_ = {}
    keywords_.update(json.loads(keyword_string))
    
    return keywords_
