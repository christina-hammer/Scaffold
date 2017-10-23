#Christina Hammer
#Last Edit: 10/24/2017
#helper_functions.py

#This collection of functions are used to perform necessary functions that aren't part of the main class structure of the program

import nltk
import json
from datetime import datetime
import re
import codecs

def parse_and_tokenize_document_body(input_article):
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    phrase_strings = sent_detector.tokenize(input_article.strip())    
    return phrase_strings

def read_from_url(url):
    #check for valid url
    #read in text body from url
    #make sure text body is valid input to create scaffold
    input_article = "read text body from url"
    return parse_and_tokenize_document_body(input_article)
                       

#input: "infile" - string
#output: list of strings
#purpose: open file containing text article to be scaffolded and reads text into a list of of strings, seperated by phrase
def read_from_txt_file(in_file):
    
    try:
        f = codecs.open(in_file, "r", encoding = 'utf-8', errors = 'ignore')
    except IOError:
        sys.exit("Cannot Open File")
    try:    
        input_article = f.read()
    except IOError:
        sys.exit("Cannot Read File")
    
    #list of strings
    return parse_and_tokenize_document_body(input_article)

def process_input(input_string):    
    #if input_string is in url format: read_from_url(url)
    #if input_string is in .txt format: 
    return read_from_text_file(input_string)
    
    
#input: "scaffold" - Scaffold object
#output: none
#purpose: transfers content of scaffold object into a text file 
def write_to_output_file(scaffold):
    
    test_dt = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    of_name = str("scaffold" + test_dt + ".txt")
    
    outf = open("output/" + of_name, 'w')
    config = set()
    #config.add("p")
    #config.add("l")
    #config.add("n")
    #config.add("a")
    scaffold_output = scaffold.display(config)
    
    outf.write(scaffold_output)        
    outf.close() 
        
    return

#input: none
#output: dictionary of string,string pairs
#purpose: populate a dictionary of keywords from a json file to be used in tagging  
def load_keywords():
    #write code to load JSON file into dictionary    
    keyword_json = open("keywords.json", encoding = 'utf8')
    keyword_string = keyword_json.read() 
    keywords_ = {}
    keywords_.update(json.loads(keyword_string))
    
    
    return keywords_