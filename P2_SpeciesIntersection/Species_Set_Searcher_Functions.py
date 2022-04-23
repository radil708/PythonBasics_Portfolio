import pandas as pd
from datetime import datetime


def get_all_unique_across_all_sets(dataframe: pd.DataFrame) -> list:
    '''
    Obtain all unique values from a dataframe
    :param dataframe: the dataframe that represents
        data from target file
    :return: (list) containing every unique values
        across the entire dataframe
    '''

    all_unique_all_sets = []

    for col in dataframe:
        all_unique_all_sets.extend(dataframe[col])

    return list(set(all_unique_all_sets))


def get_list_all_col_unique(dataframe: pd.DataFrame) -> list:
    '''
    Creates a list of lists. Each list component represents
        one column from the dataframe. Any duplicate elements
        are filtered out, leaving only the unique elements.
    :param dataframe: The dataframe that represents the data
        obtained from the target file.
    :return: (list) A list of lists, where each internal list
        represents the unique values per column of the
        dataframe.
    '''

    list_all_col_sets = []

    for col in dataframe:
        list_all_col_sets.append(list((dataframe[col].unique())))

    return list_all_col_sets


def check_in_set(value: str, col_set: list) -> bool:
    '''
    A simple function that returns true is the value is in
        the col_set and false otherwise.
    :param value: (str) the value to check if present in the col_set list
    :param col_set: (list) the list to check for the existance of the value
    :return: (bool) True if the value exists in the list, false otherwise
    '''
    if value in col_set:
        return True
    else:
        return False


def write_up(all_unique: list, appear_across_all: list) -> None:
    '''
    This function writes the results of the search to a file
    :param all_unique: (list) all the unique value across the dataframe
    :param appear_across_all: all the values that appear in every column
        of the dataframe
    :return: None
    '''
    file_entry = ["AFTER ACTION REPORT FOR {}:\n\n".format(datetime.now())]
    file_entry.append("Number of Unique values across all sets = {}\n\n".format(len(all_unique)))
    file_entry.append("Number of values that appear across all columns/sets = {}\n".format(len(appear_across_all)))
    file_entry.append("VALUES:\n")

    f_name = datetime.now().strftime("Results %Y-%m-%d %H_%M_%S" + ".txt")
    with open(f_name, 'w') as results_file:
        for entry in file_entry:
            results_file.write(entry)
        counter = 1
        for element in appear_across_all:
            results_file.write("{}.) {}\n".format(counter, element))
            counter += 1
