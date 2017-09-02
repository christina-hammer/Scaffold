#Christina Hammer
#Last Edit: 9/01/2017
#PersonCategorizer.py

#this is called person instead of name because I want it to identify when a name is used to identify a person. An article about Bill Gates is an article about a person. An article about hte Bill Gates Foundation is not an article about a person. Bill Gate is a name in both but only a person in one.
class PersonCategorizer:
    
    def __init__(self):
        self.tag = "PSN"
        
        #last names from persons that have been evaluated by the higher-authority ProperNoun Categorizer confirmed as such within the bounds of whatever pass values have been assigned
        self.confirmed_entries = []
        return
    
    def check_confidence(self, text, phrase):
        return (self.tag, 0)