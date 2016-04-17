#Christina Hammer 4/16/2016
#Scaffold 


import nltk
import string
import nltk.tag
from nltk import tokenize
from nltk import pos_tag

import sys

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
        self.pronouns = set()
        
    def addQuote(self, new_quote):
        self.quotes.append(new_quote)
        
    def addStat(self, new_stat):
        self.stats.append(new_stat)
       
    def addLine(self, new_line):
        self.body.append(new_line)

    def addPronouns(self, lst):
        punct = set(string.punctuation)
        for pn in lst:
            pn = ''.join(ch for ch in pn if ch not in punct)
            self.pronouns.add(pn)

    def sentenceCount(self):
        return len(self.body)
    
    def statCount(self):
        return len(self.stats)
    
    def quoteCount(self):
        return len(self.quotes)
    
    def pnCount(self):
        return len(self.pronouns)
    
    def show_full_line(self, quote_num):
            return self.body[quote_num] + "[line: " + str(quote_num) + "]" + "\n" 
    
    def writeQuotes(self):
        outp = ""
        lines_to_print = set()
        for q in self.quotes:
            lines_to_print.add(q.line_num)
            #print(q.content, "[line: ", q.line_num, "]","\n")
            #print(self.body[q.line_num], "[line: ", q.line_num, "]","\n")
        for num in lines_to_print:
            outp = outp + self.show_full_line(num) + "\n\n"
        return outp
    
    def writeStats(self):
        outp = ""
        for s in self.stats:
            outp = outp + s.content+ "[line: "+ str(s.line_num) + "]"+ "\n\n"
            #print(s.content, "[line: ", s.line_num, "]","\n")
        return outp
            
    def writePns(self):
        outp = ""
        sorted_pn = sorted(self.pronouns)
        for pn in sorted_pn:
            outp = outp + pn + "\n"
            #outp = outp + '<a href="http://www.en.wikipedia.org/wiki/'+ pn +'"> '+ pn +'</a>'+ "\n"
            #print(pn)
        return outp    
    
    def provide_context(self, quote_line):
        if quote_line > 0:
            print(self.body[quote_line - 1], "\n")
            
        print(self.body[quote_line], "\n")
        
        if quote_line < (len(self.body) - 1):
            print(self.body[quote_line + 1], "\n")
            
    
    
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
           

def main_parse(article_file):
    
    try:
        f = open(article_file)
    except IOError:
        sys.exit("Cannot Open File")
    
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
        
        ##process below templated after 
        ##http://stackoverflow.com/questions/17669952/finding-proper-nouns-using-nltk-wordnet
        tagged_sent = nltk.pos_tag(phrase.split())
        pns = [word for word,pos in tagged_sent if pos == 'NNP']
        
        art.addPronouns(pns)
        
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
        
    return art       


title = input('Please enter the name of the text file:')
article_obj = main_parse(title)

of_name = input('Please the name of your Scaffold file:')

outf = open(of_name, 'w')

scaffold = "Total number of statements: " + str(article_obj.sentenceCount())+"\n\n"

scaffold = scaffold + "====QUOTES====\n"
scaffold = scaffold + "Total number of quotes:"+str(article_obj.quoteCount())+"\n\n"
scaffold = scaffold + article_obj.writeQuotes() + "\n\n"

scaffold = scaffold + "====STATS====\n"
scaffold = scaffold + "Total number of stats:"+str(article_obj.statCount())+"\n\n"
scaffold = scaffold + article_obj.writeStats() + "\n\n"

scaffold = scaffold + "====PEOPLE,=PLACES,=AND=THINGS====\n"
scaffold = scaffold + "Total number of proper nouns:"+str(article_obj.pnCount())+"\n\n"
scaffold = scaffold + article_obj.writePns() + "\n\n"

outf.write(scaffold)

outf.close()

