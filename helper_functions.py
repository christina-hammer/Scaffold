#Christina Hammer
#Last Edit: 09/17/2017
#helper_functions.py

from Phrase import *
import nltk
import json
from datetime import datetime
import re

KEYWORDS = {}

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

def month_used_as_gpe(token_text):
    return token_text in {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"}

def tree_to_tuple(ne_token):
    
    token_text = ""
    
    if ne_token.label() == "PERSON":        
        for i in range(0, (len(ne_token)-1)):
            token_text = str(ne_token[i][0]) + " "           
        
        lname = ne_token[len(ne_token)-1][0]        
        return ((lname, token_text), ne_token.label())
        
    for t in ne_token:
        token_text = token_text + str(t[0]) + " "    
    
    token_text = token_text[:-1]

    if ne_token.label() == "GPE":
        if month_used_as_gpe(token_text):
            
            return (token_text, "DATETIME")
        else:
            return (token_text, ne_token.label())
    
    return (token_text, "NAMED_ENTITY")

def phrase_maker(phrase_str):    
    tokenized_phrase = nltk.word_tokenize(phrase_str)
    tagged_phrase = nltk.pos_tag(tokenized_phrase)
    ne_chunk_phrase = nltk.ne_chunk(tagged_phrase)
    
    tokens = [] #list of tagged tuples
    for token in ne_chunk_phrase:
        if type(token) is nltk.tree.Tree:            
            tokens.append(tree_to_tuple(token))
        else:
            if (token[0] in KEYWORDS):                
                token = (token[0], KEYWORDS[token[0]])                
            tokens.append(token)    
    phrase = Phrase(tokens)    
    return phrase
   
def load_keywords():
    #write code to load JSON file into dictionary    
    keyword_json = open("keywords.json")
    keyword_string = keyword_json.read()
    KEYWORDS.update(json.loads(keyword_string))
    
    return

def am_pm_follows(tokens, index):
    if index > (len(tokens) - 2):
        return False
    return tokens[index + 1][0] == "p.m." or tokens[index + 1][0] == "a.m."
    

def value_is_date_time(tokens, index):
    #non-round hour times
    if am_pm_follows(tokens, index):
        if re.search("/d:/d/d", (tokens[index][0])):
            return True
        if 0 < float(tokens[index][0]) and float(tokens[index][0]) < 13:        
            return True  
    elif re.match("/d/d/d/d", tokens[index][0]):
        return True
    
    return False