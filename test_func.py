from functions import *

def input_mutch(dictionary):
    out_dict = {}
    number = input_number( "Количество людей" )
    for i in range( number ):
        add = input_numbers( dictionary, 'Выбор' )
        for key, val in dictionary:
            out_dict[add] = val
        dictionary.pop( add )
    return out_dict, number

print(input_mutch(org))