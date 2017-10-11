#Christina Hammer
#Last Edit: 10/08/2017
#helper_functions.py

<<<<<<< HEAD
#This collection of functions are used to perform necessary functions that aren't part of the main class structure of the program

=======
>>>>>>> 26e444ec1a5ccd11f2f8afead90bf4077223b415
import nltk
import json
from datetime import datetime
import re

<<<<<<< HEAD
#input: "infile" - string
#output: list of strings
#purpose: open file containing text article to be scaffolded and reads text into a list of of strings, seperated by phrase
=======
>>>>>>> 26e444ec1a5ccd11f2f8afead90bf4077223b415
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

#input: "scaffold" - Scaffold object
#output: none
#purpose: transfers content of scaffold object into a text file 
def write_to_output_file(scaffold):
    
    test_dt = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    of_name = str("scaffold" + test_dt + ".txt")
    
    outf = open("output/" + of_name, 'w')
    scaffold_output = scaffold.display()
    
    outf.write(scaffold_output)        
    outf.close() 
        
    return
<<<<<<< HEAD

#input: none
#output: dictionary of string,string pairs
#purpose: populate a dictionary of keywords from a json file to be used in tagging  
=======
  
>>>>>>> 26e444ec1a5ccd11f2f8afead90bf4077223b415
def load_keywords():
    #write code to load JSON file into dictionary    
    keyword_json = open("keywords.json")
    keyword_string = keyword_json.read() 
    keywords_ = {}
    keywords_.update(json.loads(keyword_string))
    
<<<<<<< HEAD
    return keywords_
=======
    return keywords_
>>>>>>> 26e444ec1a5ccd11f2f8afead90bf4077223b415
