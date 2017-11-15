#Chrstina Hammer 
#Last Edit: 11/15/2017
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
    def get_datetimes(self):
        dt = {}
        for l in self.datetimes:
            dt[l+1] = self.article[l]
            
        return dt
    
    def get_quotes(self):
        q = {}
        for l in self.quotes:
            q[l+1] = self.article[l]
            
        return q
    
    def get_num_data(self):
        n = {}
        for l in self.numerical_data:
            n[l+1] = self.article[l]
            
        return n
    
    def get_article(self):
        a = ""
        for i in range(0, len(self.article)):
            a = a + str(i+1) + ". " + self.article[i] + "\n"
        return a
    
    def display(self, configuration):
        
        print_all = (len(configuration) == 0) #bool
        
        display_string = ""
        if ("p" in configuration or print_all):            
            display_string = display_string  + "PEOPLE:\n\n"
            if (len(self.persons) == 0):
                display_string = display_string + "No named persons found in text\n\n"
            else:
                for p in self.persons:
                    display_string = display_string + self.persons[p][0] + p + " "*(self.longest_entry + 4 - (len(p) + len(self.persons[p][0]))) + "Lines "+ str(self.persons[p][1]) + "\n"
                
        if ("l" in configuration or print_all):  
            display_string = display_string + "\nLOCATIONS:\n\n"        
            if (len(self.locations) == 0):
                display_string = display_string + "No named locations found in text\n\n"
            else:
                for l in self.locations:
                    display_string = display_string + l + " "*(self.longest_entry + 4 - len(l)) + "Lines "+ str(self.locations[l]) + "\n"
            
        if ("n" in configuration or print_all):    
            display_string = display_string + "\nOTHER NAMED SUBJECTS:\n\n"
            if (len(self.named_entities) == 0):
                display_string = display_string + "No other named subjects found in the text\n\n"
            else:            
                for n in self.named_entities:
                    display_string = display_string + n + " "*(self.longest_entry + 4 - len(n)) + "Lines "+ str(self.named_entities[n]) + "\n"
        
        if ("q" in configuration or print_all):    
            display_string = display_string + "\nQUOTES:\n\n"
            if (len(self.quotes) == 0):
                display_string = display_string + "No quotes found in the text\n\n"
            else:                        
                for q in self.quotes:
                    display_string = display_string + str(self.article[q]) + " [Line "+ str(q) +"]\n\n"
            
        if ("t" in configuration or print_all):   
            display_string = display_string + "\nEVENT DATES & TIMES:\n\n"
            if (len(self.datetimes) == 0):
                display_string = display_string + "No specific dates or times found in the text\n\n"
            else:                        
                for dt in self.datetimes:
                    display_string = display_string + str(self.article[dt]) + " [Line "+ str(dt) +"]\n\n"
                
        if ("d" in configuration or print_all):   
            display_string = display_string + "\nNUMERICAL DATA:\n\n"
            if (len(self.numerical_data) == 0):
                display_string = display_string + "No numerical data figures found in the text\n\n"
            else:                 
                for d in self.numerical_data:
                    display_string = display_string + str(self.article[d]) + " [Line "+ str(d) +"]\n\n"
            
        if ("a" in configuration or print_all):   
            display_string = display_string + "\nORIGINAL ARTICLE:\n\n"
            for i in range(0, len(self.article)):
                display_string = display_string + str(i) + ". " + str(self.article[i]) + "\n"
                
        return display_string