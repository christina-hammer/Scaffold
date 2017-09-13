##Chrstina Hammer 
#Last Edit: 09/13/2017
##Scaffold.py

#holds the final breakdown, so to speak
#this stores things. it can be added to. contents already added not intended to be edited
#singleton
class Scaffold:
    
    def __init__(self):
        self.locations = {}        
        self.people = {}
        self.named_entities = {}
        
        self.data_points = [] #int position of phrases in text
        self.datetimes = [] #int position of phrases in text
        self.quotes = [] #int positions of phrases in the text
        
        self.article = [] #strings
        
        #return string of formatted results for printing/text files/general oggling
    def display(self):
        
        display_string = "PEOPLE:\n\n"
        for p in self.people:
            display_string = display_string + p + "\n"
            
        display_string = display_string + "\nLOCATIONS:\n\n"
        for l in self.locations:
            display_string = display_string + l + "\n"
            
        display_string = display_string + "\nNAMED ENTITIES:\n\n"
        for g in self.named_entities:
            display_string = display_string + g + "\n"
            
        display_string = display_string + "\nQUOTES:\n\n"
        for q in self.quotes:
            display_string = display_string + self.article[q] + " [Line "+ q +"]\n\n"
            
        display_string = display_string + "\nEVENT DATES & TIMES:\n\n"
        for dt in self.datetimes:
            display_string = display_string + self.article[dt] + " [Line "+ dt +"]\n\n"
            

        display_string = display_string + "\nDATA POINTS:\n\n"
        for d in self.data_points:
            display_string = display_string + self.article[d] + " [Line "+ d +"]\n\n"
        
        display_string = display_string + "\nORIGINAL ARTICLE:\n\n"
        for p in self.article:
            display_string = display_string + p + "\n"
        return display_string
        
        
        
        ##add display functions. or like, something that spits out strings that I can do 
        ##shit with that breaks stuff into categories
