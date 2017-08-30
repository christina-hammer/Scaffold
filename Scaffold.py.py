##Chrstina Hammer 
#Last Edit: 8/30/2017
##Scaffold.py

##holds the final breakdown, so to speak
##this stores things. it can be added to. contents already added not intended to be edited
##singleton
class Scaffold:
    
    def __init__(self):
        self.locations = [] #ProperNouns
        self.datetimes = [] #int position of phrases in text
        self.people = [] #ProperNouns
        self.general_proper_nouns = [] #ProperNouns
        self.data_points = [] #int position of phrases in text
        self.article = [] #strings
        self.quotes = [] #int positions of phrases in the text
        
        #return string of formatted results for printing/text files/general oggling
        def display(self):
            return "Hmm maybe I'll write this function at some point.\n"
        
        
        
        ##add display functions. or like, something that spits out strings that I can do 
        ##shit with that breaks stuff into categories