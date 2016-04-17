#Christina Hammer 4/16/2016
#Scaffold 

import nltk

class Stat:
    
    def __init__(self, content, line_num):
        self.content = content        
        self.line_num = line_num   
        
    def getLine(self):
        return self.line_num
        

class Quote:
    
    def __init__(self, content, line_num):
        self.content = content
        self.line_num = line_num   
    
    def getLine(self):
        return self.line_num

class Article:
    
    def __init__(self):
        self.quotes = []
        self.stats = []
        self.body = []
        
    def addQuote(self, new_quote):
        self.quotes.append(new_quote)
        
    def addStat(self, new_stat):
        self.stats.append(new_stat)
       
    def addLine(self, new_line):
        self.body.append(new_line)

    def sentence_count(self):
        return len(body)
    
    def stat_count(self):
        return len(stats)
    
    def quote_count(self):
        return len(quotes)
    
    def print_quotes(self):
        for q in self.quotes:
            print(q.content, "[line: ", q.line_num, "]","\n" )
    
    def print_stats(self):
        for s in self.stats:
            print(s.content, "[line: ", s.line_num, "]","\n")
    
    def provide_context(self, quote_line):
        if quote_line > 0:
            print(self.body[quote_line - 1], "\n")
            
        print(self.body[quote_line], "\n")
        
        if quote_line < (len(self.body) - 1):
            print(self.body[quote_line + 1], "\n")
            
    def show_full_line(self, quote_num):
        print(self.body[quote_n])
    
def isStat(segments):
    for chunk in segments:
        if chunk.isdigit():
            return True
    return False
            
def isQuote(segments):
    for chunk in segments:
        if chunk == '"':
            return True
    return False
    

def main_parse():
    
    f = open("test_article.txt")
    input_article = f.read()
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    contents = sent_detector.tokenize(input_article.strip())
    
    art = Article()
    running_quote = ""
    collecting_quote = False;
    
    line_number = 0
    quote_start_line = 0
    
    for phrase in contents:
        #print (phrase)
        art.addLine(phrase)
        segments = phrase.strip()
        
        #if the phrase is a statistic (for now, criteria is contains number)
        if isStat(segments):
            st = Stat(phrase, line_number)
            art.addStat(st)
            
        #if the criteria is a quote (for now, criteria is contains quotations)
        if isQuote(segments):
            for segment in segments:
                #first quotation mark              
                
                if segment == '"' and collecting_quote == False:
                    running_quote = running_quote + segment
                    quote_start_line = line_number
                    collecting_quote = True                   
                ##second quotation mark (whether or not in starting phrase)
                elif segment == '"' and collecting_quote:
                    running_quote = running_quote + segment
                    q = Quote(running_quote, quote_start_line)
                    art.addQuote(q)
                    running_quote = ""
                    collecting_quote = False
                elif collecting_quote:
                    running_quote = running_quote + segment
                #else is beginning of phrase before quote or end after
                
                    
        line_number = line_number + 1
                    
    print("====QUOTES====")
    art.print_quotes()
    print("====STATS====")
    art.print_stats()           

main_parse()