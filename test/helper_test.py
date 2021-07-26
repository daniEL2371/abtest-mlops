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
from app_logger import App_Logger



class HelperTest(unittest.TestCase):

    def setUp(self) -> pd.DataFrame:
        self.helper = Helper()
        self.df = data.sample(10)
        self.df.reset_index(drop=True, inplace=True)
        self.logger = App_Logger("test.log").get_app_logger()
        self.logger.info("Testing Helper module started")


    def test_read_save_csv(self):
        saved_df = self.helper.save_csv(self.df, './test_df.csv')
        try:
          assert_frame_equal(saved_df, self.df, check_index_type=False)
          self.assertTrue(True)
          self.logger.info("Testing save_csv: passed")


        except AssertionError:
          self.assertTrue(False)
          self.logger.warning("Testing save_csv: failed")

      
        read_df = self.helper.read_csv('./test_df.csv')
        read_df.reset_index(drop=True, inplace=True)

        try:
            assert_frame_equal(self.df, read_df, check_index_type=False)
            self.assertTrue(True)
            self.logger.info("Testing read_csv: passed")


        except AssertionError:
            self.assertTrue(False)
            self.logger.info("Testing read_csv: failed")

    
    

if __name__ == '__main__':
    unittest.main()