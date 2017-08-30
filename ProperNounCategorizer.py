#Christina Hammer
#Last Edit: 8/30/2017
#ProperNounCategorizer.py

class ProperNounCategorizor:    
    def __init__(self):
               
        #default pass value
        self.pass_value = .5
        self.gen_proper_noun = GenProperNoun(self.pass_value)
        
        
    def categorize_tokens(self, phrase):        
        #"no tag found", just so I can tell whether or not a word made it through the function for db
        highest_confidence = ("NTF", 0.0)
        
        for t in phrase.tokens:
            
            if t.tag == "":
                highest_confidence = self.gen_proper_noun.highest_confidence(t, phrase)
        
            if highest_confidence.second < self.pass_value:
                t.tag = "NTF"
                t.confidence = 0.0
            else:
                t.tag = hc.first
                t.confidence = hc.second
            
        return phrase   
    
    def update_pass_value(self, new_value):
            assert(new_value >= 0)
            assert(new_value <= 1)
            ##assert float value?
            self.pass_value = new_value            
            self.gen_proper_noun.update_pass_value(new_value)
            return