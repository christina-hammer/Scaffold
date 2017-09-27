#Christina Hammer
#Last Edit: 09/27/2017

#Code written using help from:
#http://www.nltk.org/book/ch07.html

import nltk
import sys

from datetime import datetime

def merge_tokensand_flatten(ne_chunk_tree, to_be_merged):
    
    ne_chunk_list = []
    i = 0
    
    while(len(to_be_merged) > 0):
        if (i == to_be_merged[0][0]):
            r = to_be_merged[0][0]
            l = to_be_merged[0][1]
            merge_text = ""
            merge_tag = "NNP"
            
            while(r <= l):
                if(type(ne_chunk_tree[r]) is nltk.tree.Tree):
                    if ((r == i or r == l) and merge_tag == "NNP"):
                        merge_tag = ne_chunk_tree[r].label()
                    for t in ne_chunk_tree[r]:
                        merge_text = merge_text + t[0] + " "
                else:
                    merge_text = merge_text + ne_chunk_tree[r][0] + " "
            
            ne_chunk_list.append((merge_text, merge_tag))
            merge_text = ""
            merge_tag = "NNP"
            to_be_merged.pop(0)
            i = l
        else:
            ne_chunk_list.append(ne_chunk_tree[i])
            i = i + 1
        
        
        
    while(i < len(ne_chunk_tree)):
        ne_chunk_list.append(ne_chunk_tree[i])
    
    return ne_chunk_list


def is_nnp(token):
    if (type(token) is nltk.tree.Tree):
        for t in token:
            if (t[1] == "NNP" or "NNPS"):
                return True
    else:
        if (token[1] == "NNP" or "NNPS"):
            return True
    return False

def find_multi_token_nnp(ne_chunk_tree):
    multi_token_nnp = []
    leading_token = -1
    
    while(i < len(ne_chunk_tree)):
        if (i == (len(ne_chunk_tree)-1)):
            if (is_nnp(ne_chunk_tree[i]) and leading_token > -1):
                multi_token_nnp.append((leading_token, i))
        else:
            if (is_nnp(ne_chunk_tree[i])):
                if (is_nnp(ne_chunk_tree[i+1])):
                    if(leading_token == -1):
                        leading_token = i
                else:
                    if (leading_token > -1):
                        multi_token_nnp.append((leading_token, i))
                        leading_token = -1
        i = i + 1
    
    return multi_token_nnp

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
    ne_chunk_trees = [nltk.ne_chunk(phrase) for phrase in tagged_phrases]
    
    
    test_dt = datetime.now().strftime("%Y_%m_%d_%H_%M")
    test_dt = str("output/out" + test_dt + ".txt")
    out_file = open(test_dt, 'w') 
    
    named_entities = {}
    pos_occurences = {}    
    
    for ne_chunk_tree in ne_chunk_trees:
        to_be_merged= find_multi_token_nnp(ne_chunk_tree)
        ne_chunk_list = merge_tokens_and_flatten(ne_chunk_tree, to_be_merged)

        out_file.write(str(phrase) + "\n")
        
        for token in ne_chunk_list:         
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
    
    
