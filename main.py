#Christina Hammer
#Last Edit: 10/08/2017

from Scaffold import *
from ScaffoldMaker import *
import helper_functions


if __name__ == "__main__":
    in_file_name = input('Please enter the name of the text file:')
    
    phrase_strings = open_and_split_by_phrase(in_file_name)
    
    scaffold_maker = ScaffoldMaker()
        
    #takes in a list of strings (where each string is a phrase in the article)
    scaffold = scaffold_maker.create_scaffold(phrase_strings)    
    
    write_to_output_file(scaffold)
<<<<<<< HEAD
    
    
    
=======
>>>>>>> 26e444ec1a5ccd11f2f8afead90bf4077223b415
