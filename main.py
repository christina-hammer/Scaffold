#Christina Hammer
#Last Edit: 11/02/2017

from Scaffold import *
from ScaffoldMaker import *
import helper_functions


if __name__ == "__main__":
    input_name = input('Please enter the name of the text file to read input from: ')
     
    phrase_strings = process_input(input_name)
    
    scaffold_maker = ScaffoldMaker()
        
    #takes in a list of strings (where each string is a phrase in the article)
    scaffold = scaffold_maker.create_scaffold(phrase_strings)    
    
    write_scaffold_to_file(scaffold)
    
