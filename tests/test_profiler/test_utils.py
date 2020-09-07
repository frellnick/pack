#test_utils.py (profiler)

import unittest
import os
import logging
import pandas as pd

# Config
from tests import config, setup

# User Libs
from profile.utils import *


data_dir = os.path.join(os.getcwd(),'tests', 'data')


class TestProfilerUtils(unittest.TestCase):
    
    def setUp(self):
        self.fpath = os.path.join(data_dir, 'test1.csv')
        self.data = pd.read_csv(self.fpath, low_memory=False)
        self.logger = logging.getLogger(__name__)

    def test_prepare_data(self):
        self.logger.info('Test Prepare Data')
        self.logger.info(f'Data Columns (PRE): {self.data.columns}')
        prepare_data(data=self.data, filepath=self.fpath, save_copy=True)
        self.logger.info(f'Data Columns (POST): {self.data.columns}')




if __name__ == "__main__":
    unittest.main()

