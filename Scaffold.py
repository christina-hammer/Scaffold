#Chrstina Hammer 
#Last Edit: 09/17/2017
#Scaffold.py

#holds the final breakdown, so to speak
#this stores things. it can be added to. contents already added not intended to be edited
#singleton
class Scaffold:
    
    def __init__(self):
        self.locations = {}        
        self.persons = {}
        self.named_entities = {}
        
        self.data_points = [] #int position of phrases in text
        self.datetimes = [] #int position of phrases in text
        self.quotes = [] #int positions of phrases in the text
        
        self.article = [] #strings
        
        self.longest_entry = 30
        
        #return string of formatted results for printing/text files/general oggling
    def display(self):
        
        display_string = "PEOPLE:\n\n"
        
        for p in self.persons:
            display_string = display_string + self.persons[p][0] + p + " "*(self.longest_entry + 4 - (len(p) + len(self.persons[p][0]))) + "Lines "+ str(self.persons[p][1]) + "\n"
            
        display_string = display_string + "\nLOCATIONS:\n\n"
        
        for l in self.locations:
            display_string = display_string + l + " "*(self.longest_entry + 4 - len(l)) + "Lines "+ str(self.locations[l]) + "\n"
            
        display_string = display_string + "\nNAMED ENTITIES:\n\n"
        for n in self.named_entities:
            display_string = display_string + n + " "*(self.longest_entry + 4 - len(n)) + "Lines "+ str(self.named_entities[n]) + "\n"
            
        display_string = display_string + "\nQUOTES:\n\n"
        for q in self.quotes:
            display_string = display_string + self.article[q] + " [Line "+ str(q) +"]\n\n"
            
        display_string = display_string + "\nEVENT DATES & TIMES:\n\n"
        for dt in self.datetimes:
            display_string = display_string + self.article[dt] + " [Line "+ str(dt) +"]\n\n"
            

        display_string = display_string + "\nDATA POINTS:\n\n"
        for d in self.data_points:
            display_string = display_string + self.article[d] + " [Line "+ str(d) +"]\n\n"
        
        display_string = display_string + "\nORIGINAL ARTICLE:\n\n"
        for i in range(0, len(self.article)):
            display_string = display_string + str(i) + ". " + self.article[i] + "\n"
        return display_string