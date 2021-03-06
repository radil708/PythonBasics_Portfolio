#!/usr/bin/env python3
from Species_Set_Searcher_Functions import *

def main():
    # make sure the file is a csv and change this to match the name exactly including ".csv" extension
    file_name = "species_metagenomics.csv"

    try:
        df = pd.read_csv(file_name)
    except FileNotFoundError as e:
        print(e)
        print("EXITING PROGRAM")
        exit(0)

    only_unique = get_all_unique_across_all_sets(df)
    all_col_sets = get_list_all_col_unique(df)

    bool_list = []
    appear_across_all_col = []

    for each_value in only_unique:
        for each_set in all_col_sets:
            if check_in_set(each_value, each_set) == True:
                bool_list.append(True)
            else:
                bool_list.append(False)
        if all(bool_list):
            appear_across_all_col.append(each_value)
        bool_list = []

    write_up(only_unique, appear_across_all_col)


main()
