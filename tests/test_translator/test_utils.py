# test_utils.py


import unittest
import os
import logging

# Config
from tests import config, setup

# User Libs
from translator.utils import *


class TestTranslatorUtils(unittest.TestCase):
    
    def test_name_clean(self):
        n = 'Unnamed: 17'
        cn = clean_column_name(n)
        self.assertEqual(cn, 'Unnamed_17')


if __name__ == "__main__":
    unittest.main()

