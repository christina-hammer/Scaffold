#Christina Hammer
#Last Edit: 8/31/2017
#Token.py

import sys
import string
from Token import *
from helper_functions import *

class Token:    
    def __init__(self, text, position):
        self.text = ""
        self.l_punctuation = ""
        self.r_punctuation = ""
        
        #-1 = not yet determined/non-word token
        #0 = all lower
        #1 = first letter capitalized, possibly rest of word as well
        #2 = any other letter capitalized, but not first letter ex: iTunes
        
        self.caps = -1
        
        #position within the phrase
        self.position = position
        self.confidence = 0.0
        self.tag = None
        
        result = check_if_keyword(text)
        if result is not None:
            self.tag = result
            self.text = text
            return
        
        
        self._parse_string(text)
        if not(self.tag == "PNC"):
            self._check_caps() 
        return
    
    def _check_if_keyword(self, text):        
        return check_keywords(text)
            
    def _check_caps(self): 
        ##print(self.text + "\n")
        if self.text.islower():
            self.caps = 0
            return
        if self.text[0].isupper():
            self.caps = 1
            return
        
        #not all lower, but first letter not capitalized therefore
        self.caps = 2
        #write in logic to assign int for checking captialization
        return
    
    ##take string given and 
    def _parse_string(self, text):
        
        #strip out any punctuation occurring before  and after the word itself
        #ex: "Hey!" should result in r_p = " and l_p = !" and text = Hey
        #punctuation in the middle is ignored for the moment. apostrophes, hypens,etc should be left in place
        
        front = 0
        left_p = ""
        ##don't switch the order of these while loop conditions. It'll cause an index error
        while front < len(text) and text[front] in string.punctuation:
            left_p = left_p+text[front]
            front = front + 1
            
        ##if make it through the whole string without hitting any chars, it just *is* a punctuation mark
        if front == len(text):
            self.text = left_p
            self.tag = "PNC"
            self.confidence =1.0
            return
        
        self.l_punctuation = left_p
        
        back = len(text) -1 
        right_p = ""
        while text[back] in string.punctuation and back > -1:
            right_p = text[back] + right_p
            back = back -1 
        
        #text should be string given minus the beginning and end chopped off
        self.text = text[front:back+1]
        
        return