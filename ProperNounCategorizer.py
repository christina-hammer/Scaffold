#Christina Hammer
#Last Edit: 09/05/2017
#ProperNounCategorizer.py

#general proper noun-->everything that is not a location, person, date/time proper noun specifically but is likely enough to be *some* kind of propernoun. Titles, organizations, brands, publications etc. Or names of people when not used as a reference to the actual person. Like a mention of the novel "Harry Potter and the Sourcer's Stone" should not result in a person- tagged ProperNoun created for Harry Potter. The whole title is its own General Proper Noun

from Token import *
from Phrase import *
from LocationCategorizer import *
from PersonCategorizer import *

class ProperNounCategorizer:    
    def __init__(self):
            self._subcats = []
            self.tag = "GPN"
    
            self._generate_subcats()
    
    def _generate_subcats(self): 
        self._subcats.append(PersonCategorizer())
        self._subcats.append(LocationCategorizer())
        return
            
    def highest_confidence(self, token, phrase, pass_value):        
        self_confidence = self._check_confidence(token, phrase)
            
        if self_confidence < pass_value:
            return (self.tag, self_confidence)
            
        highest_confidence = (self.tag, self_confidence)
            
        for sc in self._subcats:
            hc_subcat = sc.highest_confidence(token, phrase)
            if hc_subcat[1] >= highest_confidence[1]:
                highest_confidence = hc_subcat
            
        return highest_confidence
    
    def _check_confidence(self, token, phrase):
        
        confidence = 1
        
        #if not(token.position == 0) and token.caps > 0:
            #token.confidence = 0.9 #value needs adjustment! temporary! 
            #token.tag = self.tag
            #return
        
        return confidence
        