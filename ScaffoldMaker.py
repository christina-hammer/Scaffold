#Christina Hammer 
#Last Edit: 9/13/2017
#ScaffoldMaker.py


from Scaffold import *

from Phrase import *
from helper_functions import *


class ScaffoldMaker:    
    def __init__(self):
        self._named_entities = {}
        self._persons= {}
        self._locations = {}
        self._quotation = False
        
    
    def _add_named_entity(self, new_entry, line_number):
        if not(new_entry in self._named_entities):            
            self._named_entities[new_entry] = []
        self._named_entities[new_entry].append(line_number)        
        return
    
    def _add_loc(self, new_entry, line_number):
        if not(new_entry in self._locations):
            self._locations[new_entry] = []
        self._locations[new_entry].append(line_number)        
        return 
    
    def _add_psn(self, new_entry, line_number):
        if not (new_entry in self._persons):
            self._persons[new_entry] = []
        self._persons[new_entry].append(line_number)
        return
    
    def find_semantics(self, phrase, line_number):
        
        phrase.is_quote = self._quotation
        
        for i in range(0, len(phrase.tokens)):
            if phrase.tokens[i][1] == "GPE":
                self._add_loc(phrase.tokens[i][0], line_number)
            elif phrase.tokens[i][1] == "PERSON":
                self._add_psn(phrase.tokens[i][0], line_number) 
            elif phrase.tokens[i][1] == "NAMED_ENT":
                self._add_named_entity(phrase.tokens[i][0], line_number)
            elif phrase.tokens[i][1] == "CD":
                if not phrase.is_date_time and not phrase.is_data_point:
                    if value_is_date_time(phrase.tokens, i):
                        phrase.is_date_time = True
                    else:
                        phrase.is_data_point = True
            elif phrase.tokens[i][1] == "DATETIME":
                phrase.value_is_date_time = True
                
            elif phrase.tokens[i][1] == "\"":
                if not self._quotation:
                    phrase.is_quote = True
                self._quotation = not self._quotation                
                
        return phrase
    
        
    def create_scaffold(self, ne_chunk_phrases):
        scaffold = Scaffold()
        #phrase strings should be a list of strings of phrases that compose the article
        #construct 1 wp at a time to save on space

        for i in range(0, len(phrase_strings)):
            
            scaffold.article.append(phrase_strings[i])
            phrase = phrase_maker(phrase_strings[i])
            
            self.find_semantics(phrase, i)
            
            if phrase.is_data_point:
                scaffold.data_points.append(i)
            if phrase.is_date_time:
                scaffold.datetimes.append(i)
            if phrase.is_quote:
                scaffold.quotes.append(i)
            
                
        scaffold.people = self._people
        self._people.clear()       
        
        scaffold.locations = self._locations
        self._locations.clear()
        
        scaffold.general_proper_nouns = self._general_proper_nouns
        self._general_proper_nouns.clear()  
        self.current_line = 0
        
        return scaffold
