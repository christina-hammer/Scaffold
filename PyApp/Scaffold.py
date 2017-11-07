#Chrstina Hammer 
#Last Edit: 11/06/2017
#Scaffold.py

#holds the final breakdown, so to speak
#this stores things. it can be added to. contents already added not intended to be edited
#singleton
class Scaffold:
    
    def __init__(self):
        self.locations = {}        
        self.persons = {}
        self.named_entities = {}
        
        self.numerical_data = [] #int position of phrases in text
        self.datetimes = [] #int position of phrases in text
        self.quotes = [] #int positions of phrases in the text
        
        self.article = [] #strings
        
        self.longest_entry = 30 #default, used to format display string
    
    #input: "configuration" - set of characters indicating which attributes of scaffold should be added to the display string (p = people, l = locations, n = named entities, q = quotes, t = dats/times, d = data points, a = original article). If no configuration specified, all attributes will be included in the display string
    #output: string of formatted results for printing/text files/general oggling
    #purpose: output a string containing the information from the atttributes of the Scaffold object
    def display(self, configuration):
        
        print_all = (len(configuration) == 0) #bool
        
        display_string = ""
        if ("p" in configuration or print_all):            
            display_string = display_string  + "PEOPLE:\n\n"            
            for p in self.persons:
                display_string = display_string + self.persons[p][0] + p + " "*(self.longest_entry + 4 - (len(p) + len(self.persons[p][0]))) + "Lines "+ str(self.persons[p][1]) + "\n"
                
        if ("l" in configuration or print_all):  
            display_string = display_string + "\nLOCATIONS:\n\n"        
            for l in self.locations:
                display_string = display_string + l + " "*(self.longest_entry + 4 - len(l)) + "Lines "+ str(self.locations[l]) + "\n"
        
        if ("n" in configuration or print_all):    
            display_string = display_string + "\nOTHER NAMED SUBJECTS:\n\n"
            for n in self.named_entities:
                display_string = display_string + n + " "*(self.longest_entry + 4 - len(n)) + "Lines "+ str(self.named_entities[n]) + "\n"
        
        if ("q" in configuration or print_all):    
            display_string = display_string + "\nQUOTES:\n\n"
            for q in self.quotes:
                display_string = display_string + str(self.article[q]) + " [Line "+ str(q) +"]\n\n"
            
        if ("t" in configuration or print_all):   
            display_string = display_string + "\nEVENT DATES & TIMES:\n\n"
            for dt in self.datetimes:
                display_string = display_string + str(self.article[dt]) + " [Line "+ str(dt) +"]\n\n"
            
        if ("d" in configuration or print_all):   
            display_string = display_string + "\nNUMERICAL DATA:\n\n"
            for d in self.numerical_data:
                display_string = display_string + str(self.article[d]) + " [Line "+ str(d) +"]\n\n"
        
        if ("a" in configuration or print_all):   
            display_string = display_string + "\nORIGINAL ARTICLE:\n\n"
            for i in range(0, len(self.article)):
                display_string = display_string + str(i) + ". " + str(self.article[i]) + "\n"
                
        return display_string