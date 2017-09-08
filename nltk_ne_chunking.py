#Christina Hammer
#Last Edit: 09/08/2017

#Code written using Mucho help from:
#http://www.nltk.org/book/ch07.html

import nltk
import sys
from datetime import datetime

if __name__ == "__main__":
    
    in_file_name = input('Please enter the name of the text file:')
    
    try:
        f = open(in_file_name)
    except IOError:
        sys.exit("Cannot Open File")
    
    try:    
        in_file = f.read()
    except IOError:
        sys.exit("Cannot Read File")    
    
    phrases = nltk.sent_tokenize(in_file)
    
    
    tokenized_phrases = [nltk.word_tokenize(phrase) for phrase in phrases]
    tagged_phrases = [nltk.pos_tag(phrase) for phrase in tokenized_phrases]
    ne_chunk_phrases = [nltk.ne_chunk(phrase) for phrase in tagged_phrases]
    
    #test_dt = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    #test_dt = str("out" + test_dt + ".txt")
    out_file = open("out.txt", 'w')
    
    for phrase in ne_chunk_phrases:
        out_file.write(str(phrase)+"\n")
    
    out_file.close()
    
    
