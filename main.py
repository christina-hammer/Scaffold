#Christina Hammer
#Last Edit: 10/23/2017

from Scaffold import *
from ScaffoldMaker import *
import helper_functions


if __name__ == "__main__":
    input_name = input('Please enter the name of the text file or article url:')
    
    phrase_strings = process_input(input_name)
    
    for p in phrase_strings:
        print(p)
    #scaffold_maker = ScaffoldMaker()
        
    #takes in a list of strings (where each string is a phrase in the article)
    #scaffold = scaffold_maker.create_scaffold(phrase_strings)    
    
    #write_to_output_file(scaffold)
