#Christina Hammer
#Last Edit: 10/08/2017
#PhraseMaker.py

from Phrase import *
import nltk
import re
from helper_functions import *

class PhraseMaker:
    
    def __init__(self):
        self._keywords = load_keywords()
        
    def create_phrase(self, phrase_str): 
        
        tokenized_phrase = nltk.word_tokenize(phrase_str)
        tagged_phrase = nltk.pos_tag(tokenized_phrase)
        ne_chunk_phrase = nltk.ne_chunk(tagged_phrase)
        
        
        tokens = [] #list of tagged tuples
        for token in ne_chunk_phrase:
            if type(token) is nltk.tree.Tree:            
                tokens.append(self._tree_to_tuple(token))
            else:
                if (token[0] in self._keywords):                
                    token = (token[0], self._keywords[token[0]])                
                tokens.append(token)
        phrase = Phrase(tokens)    
        return phrase        
    
    def _month_used_as_gpe(self, token_text):
        return token_text in {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"}
    
    def _tree_to_tuple(self, ne_token):
        
        token_text = ""
        
        #weed out false positives from capitalized NN tokens at beginning of sentences
        if len(ne_token) == 1 and ne_token[0][1] == "NN":
            return (ne_token[0][0], "NN")
            
        if ne_token.label() == "PERSON":        
            for i in range(0, (len(ne_token)-1)):
                token_text = str(ne_token[i][0]) + " "           
            
            lname = ne_token[len(ne_token)-1][0]        
            return ((lname, token_text), ne_token.label())
            
        for t in ne_token:
            token_text = token_text + str(t[0]) + " "    
        
        token_text = token_text[:-1]
    
        if ne_token.label() == "GPE":
            if self._month_used_as_gpe(token_text):
                
                return (token_text, "DATETIME")
            else:
                return (token_text, ne_token.label())
        
        return (token_text, "NAMED_ENTITY")    
       