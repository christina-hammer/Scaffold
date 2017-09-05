#Christina Hammer 
#Last Edit: 9/05/2017
#ScaffoldMaker.py


from Scaffold import *
from ProperNounCategorizer import *
from Token import *
from PhraseMaker import *
from DateTimeIdentifier import *


class ScaffoldMaker:    
    def __init__(self):
        self._general_proper_nouns = {}
        self._people = {}
        self._locations = {}
        self._token_categorizer = TokenCategorizer()
        
    def _run_categorizer(self, phrase):
            phrase = self._token_categorizer.categorize_tokens(phrase)
    
    def _add_gpn(self, pn_entry, line_number):
        if not(pn_entry in self._general_proper_nouns):            
            self.general_proper_nouns[pn_entry] = []
        self._general_proper_nouns[pn_entry].append(line_number)        
        return
    
    def _add_loc(self, pn_entry, line_number):
        if not(pn_entry in self._locations):
            self._locations[pn_entry] = []
        self._locations[pn_entry].append(line_number)        
        return 
    
    def _add_psn(self, full_name, lname, line_number):
        if not(lname in self._people):            
            self._people[lname] = {full_name : [line_number]}
        elif not (full_name in self._people[lname]):
            self._people[lname][full_name] = [line_number]
        else:
            self._people[lname][full_name].append(line_number)
        return
    
    def _compile_proper_nouns(self, phrase, line_number):
        pn_entry = ""
        last_tag = ""
        for i in range(0, len(phrase.proper_nouns)+1):
            if i < len(phrase.proper_nouns):
                if last_tag == "GTL":
                    self._add_gpn(pn_entry)
                    last_tag = phrase.tokens[phrase.proper_nouns[i]].tag
                    pn_entry = phrase.tokens[phrase.proper_nouns[i]].text
                    continue
                if last_tag == prase.tokens[phrase.proper_nouns[i]].tag:
                    if not(phrase.proper_nouns[i-1]+1 == phrase.proper_nouns[i]):
                        if connected_proper_nouns(phrase.tokens, prase.proper_nouns[i-1], phrase.proper_nouns[i]):
                            for j in range(phrase.proper_nouns[i-1]+1, phrase.proper_nouns[i]+1):
                                pn_entry = pn_entry + phrase.tokens[j] + " "
                                continue
                    else:
                        pn_entry = pn_entry + phrase.proper_nouns[i].text + " "
                        continue
                        
            if last_tag == "PSN":              
                self._add_psn(pn_entry, phrase.tokens[wp.proper_nouns[i-1]].text, line_number)
                pn_entry = ""
            elif last_tag == "TTL":
                #if title from last token attached to a name, make it part of a person PN
                #if stray title with no name attached, not a specific person should be a GPN    
                if i > len(phrase.proper_nouns): 
                    self._add_gpn(pn_entry)                
                    continue
                if not(phrase.proper_nouns[i-1]+1 == phrase.proper_nouns[i]):
                    self._add_gpn(pn_entry, line_number)
                    pn_entry = ""
            elif last_tag == "LOC":
                self._add_loc(pn_entry, line_number)                
                pn_entry = ""                
            elif last_tag == "GPN":
                self._add_gpn(pn_entry, line_number)                
                pn_entry = ""
            else:
                print("Invalid Tag assignment " + phrase.tokens[wp.proper_nouns[i-1]].tag + " given to token: " + phrase.tokens[phrase.proper_nouns()[i-1]].text + "\n")
                sys.exit("Cannot add proper noun object\n")
                return  
            if i < len(phrase_.proper_nouns):
                last_tag = phrase.tokens[phrase.proper_nouns[i]].tag
                pn_entry = pn_entry + phrase.tokens[phrase.proper_nouns[i]].text + " "
                     
        return
        
    def create_scaffold(self, phrase_strings):
        scaffold = Scaffold(self.phrase_strings)
        #phrase strings should be a list of strings of phrases that compose the article
        #construct 1 wp at a time to save on space
        load_keywords()
        for i in range(0, len(phrase_strings)):
            scaffold.article.append(phrase_strings[i])
            phrase = self.string_to_phrase(phrase_strings[i])
            
            self._run_categorizer(phrase) #this should tag all tokens as well as noting quotes/numbers
            if not(phrase.proper_nouns.empty()):
                self._compile_proper_nouns(phrase, scaffold)
                
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
        
        close_keywords()
        return scaffold