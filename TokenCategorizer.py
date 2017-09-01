#Christina Hammer
#Last Edit: 8/31/2017
#TokenCategorizer.py

from Token import *
from Phrase import *
from ProperNounCategorizer import *
from helper_functions import *
from NumberContextIdentifier import *

class TokenCategorizor:    
    def __init__(self):
               
        #default pass value
        self.pass_value = .5
        
        self._proper_noun_cat = ProperNounCategorizer()
        self._number_context_identifier = NumberContextIdentifier()
        
        return
    
    def categorize_tokens(self, phrase):
        
        for t in phrase.tokens:
            if t.tag is None:
                if is_digit(t.text[0]):
                    t.tag = self.number_context_identifier.tag_number()
                else if t.caps > 0:
                    self.proper_noun_cat.categorize_token(t, phrase)
        
        return
        
        
        