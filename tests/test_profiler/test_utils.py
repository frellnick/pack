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

    def test_prepare_data(self):
        prepare_data(data=self.data, filepath=self.fpath)



if __name__ == "__main__":
    unittest.main()

