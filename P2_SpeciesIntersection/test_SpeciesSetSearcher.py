import unittest
from Species_Set_Searcher_Functions import *
import pandas as pd

class testIntersection(unittest.TestCase):

    def test_get_unique_from_test_file(self):
        df = pd.read_csv("test_file_1.csv")
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

        appear_across_all_col = sorted(appear_across_all_col)
        self.assertEqual(['C','X'], appear_across_all_col)

    def test_get_from_empty_file(self):
        df = pd.read_csv("test_empty_file_test.csv")
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

        appear_across_all_col = sorted(appear_across_all_col)
        self.assertEqual([], appear_across_all_col)


if __name__ == "__main__":
    unittest.main(verbosity=3)