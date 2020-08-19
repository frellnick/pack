# test_profile.py


import unittest
import os
import logging

# Config
from tests import config, setup

# User Libs
from profile import Profiler
from translator import OracleTranslator


class TestProfilerActions(unittest.TestCase):
    
    def setUp(self):
        setup(log=True)
        self.logger = logging.getLogger(__name__)

        self.data_dir = os.path.join(os.getcwd(),'tests', 'data')
        assert len(os.listdir(self.data_dir)) > 0, f'Data files missing from data directory {self.data_dir}'
        self.data_paths = [os.path.join(self.data_dir, fname) for fname in os.listdir(self.data_dir)]

        self.profilers = []
        for f in self.data_paths:
            prf = Profiler()
            prf.load_csv(f, low_memory=False)
            self.profilers.append(prf)

        


    def test_make_oracletranslator(self):
        self.logger.info('Test: Make OracleTranslator Instance')
        tlr = OracleTranslator()


    def test_oracletranslation(self):
        self.logger.info('Test: Translate profile with OracleTranslator')
        profile = self.profilers[0].profile 
        tlr = OracleTranslator()

        translation = tlr(profile)
        self.logger.info(f'Translation: {translation}')

        self.assertEqual(len(translation), 4)


if __name__ == "__main__":
    unittest.main()