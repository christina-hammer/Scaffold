#Christina Hammer
#Last Edit: 09/05/2017
#LocationCategorizer.py

class NameCategorizer:
    
    def __init__(self):
        
        self.tag = "LOC"
        self.confirmed_entries = []
        
        return
    
    def check_confidence(self, text, phrase):
        return (None, 0)