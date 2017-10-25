#Christina Hammer
#Last Edit: 10/24/2017
#helper_functions.py

#This collection of functions are used to perform necessary functions that aren't part of the main class structure of the program

import nltk
import json
from datetime import datetime
import re
import codecs
import urllib
import re
from six.moves.urllib.request import urlopen

def parse_and_tokenize_document_body(input_article):
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    phrase_strings = sent_detector.tokenize(input_article.strip())    
    return phrase_strings

def read_from_url(url):
    
    #read in text body from url
    #make sure text body is valid input to create scaffold
    
    input_article = urlopen(url)
    contents = input_article.read()
    #return parse_and_tokenize_document_body(input_article)
    return contents
                       

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

def check_valid_url(input_url):
    
    #url validation regex template found at https://stackoverflow.com/questions/7160737/python-how-to-validate-a-url-in-python-malformed-or-not
    
    url_regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)    
    
    valid = url_regex.match(input_url)
    if valid:
        return True
    
    return False

def process_input(input_string):   
       
    if (check_valid_url(input_string) ):
        return read_from_url(input_string)    
    #if input_string is in .txt format: 
    return read_from_text_file(input_string)
    
    
#input: "scaffold" - Scaffold object
#output: none
#purpose: transfers content of scaffold object into a text file 
def write_to_output_file(scaffold):
    
    test_dt = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    of_name = str("scaffold" + test_dt + ".txt")
    
    outf = open("output/" + of_name, 'w')
    #config = set()
    #config.add("p")
    #config.add("l")
    #config.add("n")
    #config.add("a")
    #scaffold_output = scaffold.display(config)
    
    #outf.write(scaffold_output)       
    outf.write(str(scaffold) )
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