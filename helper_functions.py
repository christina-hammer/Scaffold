#Christina Hammer
#Last Edit: 09/13/2017
#helper_functions.py

from Phrase import *
import nltk
import json

KEYWORDS = None

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

def write_to_output_file(of_name, scaffold):
    
    outf = open(of_name, 'w')
    scaffold_output = scaffold.display()
        
    outf.write(scaffold_output)        
    outf.close() 
        
    return

def tree_to_tuple(ne_token):
    token_text = ""
    for t in token:
        token_text = token_text + str(t[0]) + " "    
    try:
        token_text = token_text[:-1]
    
    specified_entities = {"GPE", "PERSON"}
    if token.label() not in specified_entities:
        return (token_text, "NAMED_ENTITY")
    
    return (token_text, token.label())

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
                token[1] = KEYWORDS[token[0]]
        tokens.append(token)
    
    phrase = Phrase(tokens)    
    return phrase
   
def load_keywords():
    #write code to load JSON file into dictionary    
    keyword_json = open("keywords.json")
    keyword_string = keyword_json.read()
    KEYWORDS = keyword_string.loads(keyword_string)[0]  
        
    return

def value_is_date_time(tokens, index):
    #non-round hour times
    if not tokens[index].isdigit():
        return check_time_format(tokens[index])
            
    if not float(tokens[index]).is_integer():
        return False
    
    if 0 < float(tokens[index]) and float(tokens[index]) < 13:
        if index > (len(tokens) - 2):
            return False
        if tokens[index + 1] == "p.m." or tokens[index + 1] == "a.m.":
            return True        
    elif int(tokens[index]) > 1000 and int(tokens[index]) < 10000:
        return True
    
    return False
