#Christina Hammer
#Last Edit: 8/30/2017
#GeneralProperNoun.py

#general proper noun-->everything that is not a location, person, date/time proper noun specifically but is likely enough to be *some* kind of propernoun. Titles, organizations, brands, publications etc. Or names of people when not cleary used as a reference to the actual person. Like a mention of the novel "Harry Potter and the Sourcer's Stone" should not result in a person- tagged ProperNoun created for Harry Potter. The whole title is its own General Proper Noun

from Token import *
from Phrase import *

class GeneralProperNoun:    
    def __init__(self, pass_value):
            self._subcats = []
            self.tag = "GPN"
            self._pass_value = pass_value    
    
    def update_pass_value(self, new_value):
            self.pass_value = new_value
            for sc in self.subcats:
                sc.update_pass_value(new_value)
            
    #populates subcats dictionary with instances of subcategory checkers
    #pure virtual function (I think)
    #populates subcats dictionary with instances of subcategory checkers
    def _generate_subcats(self):   
        
        #self._subcats.append(Name(self._pass_value))
        #self._subcats.append(DateDescriptor(self._pass_value))
        #self._subcats.append(Nationality(self._pass_value))
        #self._subcats.append(Location(self._pass_value))
        return
            
    #at this point, token is AT LEAST a proper noun of some kind
    def highest_confidence(self, token, phrase):        
        self_confidence = self._check_confidence(token, phrase)
            
        if self_confidence < self._pass_value:
            return (self.tag, self_confidence)
            
        self._generate_subcats()
        highest_confidence = (self.tag, self_confidence)
            
        for sc in self.subcats:
            #value of the highest confidence level for subcategory in question
            #includes current subcategory as well as all levels of children
            hc_subcat = sc._highest_confidence(token, phrase)
            if hc_subcat.second >= highest_confidence.second:
                highest_confidence = hc_subcat
            
        return highest_confidence
        
    #need to determine algorithm to decide float representing confidence that word is 
    #a proper noun of some kind
    ##double underscore if end up making subclasses that need to overwrite###
    
    def _check_confidence(self, token, phrase):
        
        confidence = 0.0
        
        if not(token.position == 0) and token.caps > 0:
            token.confidence = 0.9 #value needs adjustment! temporary! 
            token.tag = self.tag
            return
            
            
        #elif word.
        #if capitalized word is in the middle of a phrase (not at beginning of sentence) then it's a proper noun with the exception of "I" "I'm" 
        
        return confidence
        