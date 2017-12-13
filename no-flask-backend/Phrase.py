#Christina Hammer
#Last Edit: 11/06/2017

import sys
import string

       
#created with basic contents of phrase, object can be modified as analyses are run
class Phrase:   
    def __init__(self, tokens_):
        
        #tokens is a list of tuples of tagged tokens, some with POS tags, some with ne tags, some with keyword tags. All are pairs of strings ("token", "TAG")
        self.tokens = tokens_       
        self.is_quote = False        
        self.is_numerical_data = False
        self.is_date_time = False
        