#Christina Hammer 
#Last Edit: 10/08/2017
#ScaffoldMaker.py


from Scaffold import *
from Phrase import *
from PhraseMaker import *

class ScaffoldMaker:    
    def __init__(self):
        self._named_entities = {}
        self._persons= {}
        self._locations = {}
        self._quotation = False
        self._longest_entry = 0
        self._phrase_maker = PhraseMaker()
        
    
    def _add_named_entity(self, new_entry, line_number):
        if len(new_entry) > self._longest_entry:
            self._longest_entry = len(new_entry)
        if not(new_entry in self._named_entities):            
            self._named_entities[new_entry] = []
        self._named_entities[new_entry].append(line_number)        
        return
    
    def _add_loc(self, new_entry, line_number):
        if len(new_entry) > self._longest_entry:
            self._longest_entry = len(new_entry)        
        if not(new_entry in self._locations):
            self._locations[new_entry] = []
        self._locations[new_entry].append(line_number)        
        return 
    
    def _add_psn(self, new_entry, line_number):
        if (len(new_entry[0]) + len(new_entry[1])) > self._longest_entry:
            self._longest_entry = (len(new_entry[0]) + len(new_entry[1]))  
            
        if not (new_entry[0] in self._persons):
            self._persons[new_entry[0]] = (new_entry[1],[])
        self._persons[new_entry[0]][1].append(line_number)
        return
    
    def _am_pm_follows(self, tokens, index):
        if index > (len(tokens) - 2):
            return False
        return tokens[index + 1][0] == "p.m." or tokens[index + 1][0] == "a.m."
        
    
    def _value_is_date_time(self, tokens, index):
        #non-round hour times
        if self._am_pm_follows(tokens, index):
            if re.search("/d:/d/d", (tokens[index][0])):
                return True
            if 0 < float(tokens[index][0]) and float(tokens[index][0]) < 13:        
                return True  
        elif re.match("/d/d/d/d", tokens[index][0]):
            return True
        
        return False     
    
    def find_semantics(self, phrase, line_number):
        
        phrase.is_quote = self._quotation
        
        for i in range(0, len(phrase.tokens)):
            
            if phrase.tokens[i][1] == "GPE":
                
                self._add_loc(phrase.tokens[i][0], line_number)
            elif phrase.tokens[i][1] == "PERSON":
                
                self._add_psn(phrase.tokens[i][0], line_number) 
            elif phrase.tokens[i][1] == "NAMED_ENTITY" or phrase.tokens[i][1] == "NNP":
                
                self._add_named_entity(phrase.tokens[i][0], line_number)
            elif phrase.tokens[i][1] == "CD":
                
                if not phrase.is_date_time and not phrase.is_data_point:
                    if self._value_is_date_time(phrase.tokens, i):
                        phrase.is_date_time = True
                    else:
                        phrase.is_data_point = True
            elif phrase.tokens[i][1] == "DATETIME":
                
                phrase.is_date_time = True
                
            elif phrase.tokens[i][1] == "``" or phrase.tokens[i][1] == "''":                
                if not self._quotation:
                    phrase.is_quote = True
                self._quotation = not self._quotation                
                
        return phrase
    
        
    def create_scaffold(self, phrase_strings):
        scaffold = Scaffold()
        for i in range(0, len(phrase_strings)):
            
            scaffold.article.append(phrase_strings[i])
            phrase = self._phrase_maker.create_phrase(phrase_strings[i])
            
            self.find_semantics(phrase, i)
            
            if phrase.is_data_point:
                scaffold.data_points.append(i)
            if phrase.is_date_time:
                scaffold.datetimes.append(i)
            if phrase.is_quote:
                scaffold.quotes.append(i)
            
        scaffold.persons.update(self._persons)
        self._persons.clear()       
        
        scaffold.locations.update(self._locations)
        self._locations.clear()
        
        scaffold.named_entities.update(self._named_entities)
        self._named_entities.clear()  
        
        scaffold.longest_entry = self._longest_entry
        self._longest_entry = 0

        return scaffold