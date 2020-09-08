# test_utils.py


import unittest
import os
import logging

# Config
from tests import config, setup

# User Libs
from translator.utils import *


class TestTranslatorUtils(unittest.TestCase):
    
    def test_utflen(self):
        tstr = 'test'
        tlen = utf8len(tstr)
        self.assertEqual(tlen, 4)

    def test_sig_git(self):
        n1 = 0.0010
        n2 = 2
        n3 = 1.5

        self.assertEqual(signif_dig(n1), 4)
        self.assertEqual(signif_dig(n2), 1)
        self.assertEqual(signif_dig(n3), 2)

    def test_mantissa(self):
        n1 = 0.0010
        n2 = 2
        n3 = 1.5

        self.assertEqual(count_mantissa(n1), 3)
        self.assertEqual(count_mantissa(n2), 0)
        self.assertEqual(count_mantissa(n3), 1)

if __name__ == "__main__":
    unittest.main()

