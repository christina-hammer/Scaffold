#Christina Hammer
#Last Edit: 09/08/2017

import nltk

if __name__ == "__main__":
    
    s = "Today I saw John Green set a garbage can on fire at the Arby's in Charlotte, North Carolina"
    print("s = " + s + "\n")
    
    s = nltk.word_tokenize(s)
    print("nltk.word_tokenize(s) = " + str(s) + "\n")
    
    s = nltk.pos_tag(s)
    print("nltk.pos_tag(s) = " + str(s) + "\n")
    
    s = nltk.ne_chunk(s)
    print("nltk.ne_chunk(s) = " + str(s) + "\n")
    