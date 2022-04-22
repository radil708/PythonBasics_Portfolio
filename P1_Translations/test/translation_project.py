import os
from pathlib import Path #Need this to allow the paths to be correct irrespective of system

'''
This file contains all the functions needed to for driver file to execute
'''

DIRECTIVES_FORMAT = ['lang_in', 'lang_out', 'file_to_translate', 'file_output']

def get_lang_keys(file_name):
    '''
    Opens the file containing the metadata of the positions of the languages
    for the formation of the associative arrays
    :param file_name: (.txt) The name of the file containing metadata and language data
    :return: (dict) a dictionary where the key is the position of the language and
            the value is the language itself
    '''
    try:
        with open(file_name, mode='r') as file_in:
            meta_info = file_in.readline()
            meta_info = meta_info.strip() # remove leading or lagging spaces
            meta_info = meta_info.lstrip('METADATA') # remove string 'METADATA'
            meta_info_lst = meta_info.split(' ')
            meta_info_lst = list(filter(lambda x: x != '', meta_info_lst))
    except FileNotFoundError as e:
        print(os.getcwd())
        print(e)
        print("Please use a valid file\nEXITING PROGRAM")
        exit(0)

    dict_key_positions = {}

    for i in range(len(meta_info_lst)):
        dict_key_positions[i] = meta_info_lst[i]

    return dict_key_positions

def build_translator(file_name , keys_dict):
    '''
    Creates a dictionary containing the associative arrays. The
    keys are the language and the value is the array of each char for the
    language
    :param file_name: (.txt) file containing the raw data for the language associative array
    :param keys_dict: (dict) the output of the function get_lang_keys
    :return: (dict) a dictionary where the key is the language and the value is
        the array of characters for the language
    '''

    translator = {}

    #build empty list for each key value pair
    for each in keys_dict.values():
        translator[each] = []
    try:
        with open(file_name, mode='r') as file_in:
            file_data_as_lst = file_in.readlines()
            file_data_as_lst = file_data_as_lst[1:] # remove metadata line
            for each in file_data_as_lst:
                temp = each.strip() #remove leading and lagging characters
                temp_lst = temp.split(' ') # split by space
                temp_lst = list(filter(lambda y: y != '', temp_lst))

                for i in range(len(temp_lst)):
                    list_to_add = keys_dict[i]
                    translator[list_to_add].append(temp_lst[i])

    except FileNotFoundError as e:
        print(e)
        print("Please use a valid file\nEXITING PROGRAM")
        exit(0)

    return translator

def parse_directives(directives_file):
    '''
    Reads the directives from a directive file. The format of each line on a directive file
    is: <Language in> <Language out> <file input> <name of file output>
    :param directives_file: (.txt) file containing the directives. One line per directive.
    :return: (list) A list of dictionaries where the key is directive type and the value
            is the directive value. ex. lang_in : english, lang_out:morse etc...
    '''
    list_directives = []

    with open(directives_file, mode='r') as file_in:
        for line in file_in.readlines():
            temp = line.strip()
            temp_lst = temp.split(' ')
            dict_temp = {}

            for i in range(len(DIRECTIVES_FORMAT)):
                dict_temp[DIRECTIVES_FORMAT[i]] = temp_lst[i]

            list_directives.append(dict_temp)
    return list_directives


def run_directives(translation_dict, directives_lst, isTest = False):
    '''
    Performs the actual translation and writes to file
    :param translation_dict: (dict) the output of build_translator
    :param directives_lst: (list) the output of parse_directives
    :param isTest: (boolean) set false by defaut. If running in test
        folder, must be set True to get the correct file path
        as the current file path of the test folder cannot access
        the text_src_files directory
    :return: None
    '''
    for each in directives_lst:
        lang_in_lst = translation_dict[each['lang_in'].upper()]
        lang_out_lst = translation_dict[each['lang_out'].upper()]

        str_out = ''

        if isTest == True:
            curr_dir = os.getcwd().rstrip('test')
        else:
            curr_dir = os.getcwd()
        path_file_to_translate = Path(curr_dir + '/text_src_files/' + each['file_to_translate'])

        try:
            with open(path_file_to_translate, mode='r') as file_in:
                for line in file_in.readlines():
                    for each_char in line:
                        if each_char == '\n':
                            str_out += '\n'
                        elif each_char == ' ':
                            str_out += '/ '
                        else:
                            char_pos = lang_in_lst.index(each_char.upper())
                            str_out += lang_out_lst[char_pos] + ' '

            # Add a new line char to the end if it doesn't exist to keep consistency
            if str_out[len(str_out) - 1] != '\n':
                str_out += '\n'

        except FileNotFoundError as e:
            print(e)
            print("Please use a valid file\nEXITING PROGRAM")
            exit(0)

        with open(each['file_output'], mode='w') as file_out:
            file_out.write(str_out)

        print(f"Successfully translated {each['file_to_translate']} from {each['lang_in']}"
              f" to {each['lang_out']}... saved translation to {each['file_output']}")
