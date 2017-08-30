#Christina Hammer (unless otherwise credited)
#Last Edit: 8/30/2017

import sys
import string
from Token import *
       
##created with basic contents of phrase, object can be modified as analyses are run
class Phrase:   
    def __init__(self):
        self.tokens = []
        self.l_quote_checks = []
        self.r_quote_checks = []
        self.quote = False
        self.data_point = False
        self.proper_nouns = []
        self.datetime = False
        
    def add_token(self, token):
        if "\"" in token.l_punctuation:
            self.l_quote_checks.append(token.position)
        if "\"" in token.r_punctuation:
            self.r_quote_checks.append(token.position)

        ##replace with actual checks for these things
        #if token.tag == "NUM":
            #self.datapoint = True
        
        #if token.tag == "DT":
            #self.datetime = True
        
        #if token.tag == "POSSIBLE DT":
            #self.possible_dt_checks.append(token.position)
            
        self.tokens.append(token)
    
    def _combine_gpn_title(self, gpn_title, start, end):
        self.tokens[start].text = gpn_title
        self.tokens[start].l_punc = ""
        self.tokens[start].tag = "GTL"
        for i in range(start+1, end+1):
            self.tokens.pop(i)
        return   
    
    def _quote_or_title(self, start, end):
        i = start
        gpn_title = ""
        while i <= end:
            if (self.tokens[i].caps < 1) and not (common_connector(self.tokens[i].text)):
                self.quote = True
                return
            gpn_title =gpn_title + self.tokens[i].l_punc + self.tokens[i] +self.tokens[i].r_punc + " "
        self._combine_gpn_title(gpn_title, start, end)
        return     
    
    def _run_quote_check(self):
        if not(len(self.l_quote_checks) == len(r_quote_checks)):
            ##feedback for me while I troubleshoot, not intended for users
            printf("Unable to run quote check for phrase\n")
            return
        i = 0
        while i < len(self.l_quote_checks):
            self.tokens = quote_or_title(self.l_quote_checks[i], self.r_quote_checks[i], self.tokens)
            self.l_quote_checks.pop(i)
            self.r_quote_checks.pop(i)                
            i = i + 1        
        return


               




    
    

