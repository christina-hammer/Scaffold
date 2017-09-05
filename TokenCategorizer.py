#Christina Hammer
#Last Edit: 09/05/2017
#TokenCategorizer.py

from Token import *
from Phrase import *
from ProperNounCategorizer import *
from helper_functions import *
from NumberContextIdentifier import *

#for tokens not yet found to be keywords or in a quoted title, this is is where the brunt of token categorization takes place
class TokenCategorizer:    
    def __init__(self):
               
        #default pass value
        self.pass_value = 0
        
        self._proper_noun_cat = ProperNounCategorizer()
        self._number_context_identifier = NumberContextIdentifier()
        
        return
    
    def categorize_tokens(self, phrase):
        
        for t in phrase.tokens:
            if t.tag is None:
                if is_digit_number(t.text[0]):
                    t.tag = self.number_context_identifier.tag_number()
                elif t.caps > 0:
                    self._proper_noun_cat.highest_confidence(t, phrase, self.pass_value)
        
        return
        
        
        