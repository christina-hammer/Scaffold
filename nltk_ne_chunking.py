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
        f.close()
    except IOError:
        sys.exit("Cannot Read File")    
    
    phrases = nltk.sent_tokenize(in_file)
    
    
    tokenized_phrases = [nltk.word_tokenize(phrase) for phrase in phrases]
    tagged_phrases = [nltk.pos_tag(phrase) for phrase in tokenized_phrases]
    ne_chunk_phrases = [nltk.ne_chunk(phrase) for phrase in tagged_phrases]
    
    named_entities = {}
    NNP_non_ne = set()
    
    for phrase in ne_chunk_phrases:
        for token in phrase:
            if (type(token) is nltk.tree.Tree):
                if token.label() not in named_entities:              
                    named_entities[token.label()] = set()
                    
                for t in token:
                    named_entities[token.label()].add(t)
            else:
                if str(token[1]) == "NNP":                    
                    NNP_non_ne.add(str(token[0]))
                    
    
    test_dt = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    test_dt = str("out" + test_dt + ".txt")
    out_file = open(test_dt, 'w')
    
    for label in named_entities.keys():
        out_file.write(str(label)+": "+ str(named_entities[label]) + "\n")
        
    
    out_file.write("NNP (non named entities: )" + str(NNP_non_ne))
    
    out_file.close()
    
    
