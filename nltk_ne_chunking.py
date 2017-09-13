#Christina Hammer
#Last Edit: 09/12/2017

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
    pos_occurences = {}
    
    test_dt = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    test_dt = str("out" + test_dt + ".txt")
    out_file = open(test_dt, 'w')    
    
    #phrase is a tree or a tuple
    for phrase in ne_chunk_phrases:
        out_file.write(str(phrase) + "\n")
        for token in phrase:
            if (type(token) is nltk.tree.Tree):
                if token.label() not in named_entities:              
                    named_entities[token.label()] = set()
                    
                for t in token:
                    named_entities[token.label()].add(t)
            else:
                if token[1] not in pos_occurences:                    
                    pos_occurences[token[1]] = set()
                pos_occurences[token[1]].add(token[0])
                    
    
    for label in named_entities.keys():
        out_file.write(str(label)+": "+ str(named_entities[label]) + "\n")
        
    for pos in pos_occurences.keys():
        out_file.write(pos + ": " + str(pos_occurences[pos]) + "\n")
    
    out_file.close()
    
    
