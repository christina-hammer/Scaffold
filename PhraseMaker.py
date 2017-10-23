#Christina Hammer
#Last Edit: 10/20/2017
#PhraseMaker.py

from Phrase import *
import nltk
import re
from helper_functions import *
import string

class PhraseMaker:
    
    def __init__(self):
        self._keywords = load_keywords()
    
    #input: "create_phrase" - string
    #output: phrase object
    #purpose: creates phrase object after tokenizing and tagging the words contained in the phrase string  
    def create_phrase(self, phrase_str): 
        
        tokenized_phrase = nltk.word_tokenize(phrase_str)
        tagged_phrase = nltk.pos_tag(tokenized_phrase)
        ne_chunk_tree = nltk.ne_chunk(tagged_phrase)
        
        merge_tokens = self._find_multi_token_nnp(ne_chunk_tree) 
        ne_chunk_list = self._merge_tokens_and_flatten(ne_chunk_tree, merge_tokens)        
        
        tokens = [] #list of tagged tuples
        for token in ne_chunk_list:
            if type(token) is nltk.tree.Tree:            
                tokens.append(self._tree_to_tuple(token))
            else:
                if (token[0] in self._keywords):                
                    token = (token[0], self._keywords[token[0]])
                tokens.append(token)
        
        phrase = Phrase(tokens)    
        return phrase 
    
    #input: "ne_chunk_tree" - nltk tree of tuples and/or trees containing nltk tokens, "merge_tokens" - a list of int tuples
    #output: list of tuples/trees containing nltk tokens
    #purpose: merge tokens in ne_chunk_tree using index ranges listed in merge_tokens input arguement. flatten ne_chunk_tree from an nltk tree to a list
    def _merge_tokens_and_flatten(self, ne_chunk_tree, merge_tokens):
        
        ne_chunk_list = []
        i = 0
        
        while(len(merge_tokens) > 0):
            
            if (i == merge_tokens[0][0]):
                l = merge_tokens[0][0]
                r = merge_tokens[0][1]
                merge_text = ""
                merge_tag = "NNP"
                
                while(l <= r):  
                    
                    if(type(ne_chunk_tree[l]) is nltk.tree.Tree):
                        if ((l == i or l == r) and merge_tag == "NNP"):
                            merge_tag = ne_chunk_tree[l].label()
                        for t in ne_chunk_tree[l]:
                            merge_text = merge_text + t[0] + " "
                    else:
                        #print(merge_text + " + " + str(ne_chunk_tree[r]))
                        merge_text = merge_text + ne_chunk_tree[l][0] + " "
                    l = l + 1
                
                if (merge_text[len(merge_text)-1] == " "):
                    merge_text = merge_text[:-1]              
                
                if (merge_tag == "PERSON" ):
                    name = merge_text.rsplit(" ", 1)
                    name[0] = name[0] + " "
                    ne_chunk_list.append(((name[1], name[0]), merge_tag))
                else: 
                    ne_chunk_list.append((merge_text, merge_tag))
                    
                merge_text = ""
                merge_tag = "NNP"
                merge_tokens.pop(0)
                i = l
            else:
                ne_chunk_list.append(ne_chunk_tree[i])
                i = i + 1
        
        while(i < len(ne_chunk_tree)):        
            ne_chunk_list.append(ne_chunk_tree[i])
            i = i + 1
        
        return ne_chunk_list
    
    #input: "token" - nltk POS tagged token or nltk tree composed of nltk POS-tokens
    #output: boolean value
    #purpose: indicate whether the given tuple or tree is a Proper Noun or plural Proper noun
    def _is_nnp(self, token):
        if (type(token) is nltk.tree.Tree):
            for t in token:
                if (t[1] == "NNP" or t[1] == "NNPS"):
                    return True
        else:
            if (token[1] == "NNP" or token[1] == "NNPS"):            
                return True
        return False
    
    #input: "ne_chunk_tree" - an nltk tree containing tuples of nltk tokens and/or labeled trees of named entity chunks
    #output: a list of int tuples 
    #purpose: indicates the indices of tokens in the tree that should be merged into multi-token chunks
    def _find_multi_token_nnp(self, ne_chunk_tree):
        merge_tokens = []
        leading_token = -1
        i = 0
        
        while(i < len(ne_chunk_tree)):
            if (i == (len(ne_chunk_tree)-1)):
                if (self._is_nnp(ne_chunk_tree[i]) and leading_token > -1):
                    merge_tokens.append((leading_token, i))
            else:
                if (self._is_nnp(ne_chunk_tree[i])):
                    if (self._is_nnp(ne_chunk_tree[i+1])):
                        if(leading_token == -1):
                            leading_token = i
                    else:
                        if (leading_token > -1):
                            merge_tokens.append((leading_token, i))
                            leading_token = -1
            i = i + 1
        
        return merge_tokens    
    
    #input: "token_text" - string
    #output: bool
    #purpose: confirm whether a given string is present in the set of valid month words     
    def _month_used_as_gpe(self, token_text):
        return token_text in {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"}
    
    #input: "ne_token" - nltk tree
    #output: tuple containing string, string pair
    #purpose:   
    def _tree_to_tuple(self, ne_token):
        
        token_text = ""
        
        #weed out false positives from capitalized NN tokens at beginning of sentences
        if len(ne_token) == 1 and ne_token[0][1] == "NN":
            return (ne_token[0][0], "NN")
            
        if ne_token.label() == "PERSON":        
            for i in range(0, (len(ne_token)-1)):
                token_text = str(ne_token[i][0]) + " "           
            
            lname = ne_token[len(ne_token)-1][0]
            
            if (token_text == ""):
                return (lname, ne_token.label())
            
            return ((lname, token_text), ne_token.label())
            
        for t in ne_token:
            token_text = token_text + str(t[0]) + " "    
        
        token_text = token_text[:-1]
    
        if ne_token.label() == "GPE":
            if self._month_used_as_gpe(token_text):
                
                return (token_text, "DATETIME")
            else:
                return (token_text, ne_token.label())
        
        return (token_text, "NAMED_ENTITY")    
