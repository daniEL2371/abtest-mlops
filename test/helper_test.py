import os
import sys
import pandas as pd
import numpy as np

import unittest 
from pandas._testing import assert_frame_equal
from pandas.io.parsers import read_csv

data = pd.read_csv('../Data/data.csv')

sys.path.append(os.path.abspath(os.path.join('../scripts')))
from helper import Helper



class HelperTest(unittest.TestCase):

    def setUp(self) -> pd.DataFrame:
        self.helper = Helper()
        self.df = data.sample(10)
        self.df.reset_index(drop=True, inplace=True)


    def test_read_save_csv(self):
        saved_df = self.helper.save_csv(self.df, './test_df.csv')
        try:
          assert_frame_equal(saved_df, self.df, check_index_type=False)
          self.assertTrue(True)

        except AssertionError:
          self.assertTrue(False)
      
        read_df = self.helper.read_csv('./test_df.csv')
        read_df.reset_index(drop=True, inplace=True)

        try:
            assert_frame_equal(self.df, read_df, check_index_type=False)
            self.assertTrue(True)

        except AssertionError:
            self.assertTrue(False)
    
    

if __name__ == '__main__':
    unittest.main()