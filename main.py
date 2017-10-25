#Christina Hammer
#Last Edit: 10/24/2017

from Scaffold import *
from ScaffoldMaker import *
import helper_functions


if __name__ == "__main__":
    input_name = input('Please enter the name of the text file to read input from')
    
    
    #phrase_strings = process_input(input_name)
    phrase_strings = process_input(input_name)
    #print(phrase_strings)
    #scaffold_maker = ScaffoldMaker()
        
    #takes in a list of strings (where each string is a phrase in the article)
    #scaffold = scaffold_maker.create_scaffold(phrase_strings)    
    
    #write_to_output_file(scaffold)
    write_to_output_file(phrase_strings)
