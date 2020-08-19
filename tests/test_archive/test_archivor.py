# test_archivor.py


import unittest
import os
import logging

# Config
from tests import config, setup

# User Libs
from profile import Profiler
from translator import OracleTranslator
from archivor import agg_translations


class TestArchivorActions(unittest.TestCase):
    
    def setUp(self):
        setup(log=True)
        self.logger = logging.getLogger(__name__)

        self.data_dir = os.path.join(os.getcwd(),'tests', 'data')
        self.filenames = os.listdir(self.data_dir)
        assert len(os.listdir(self.data_dir)) > 0, f'Data files missing from data directory {self.data_dir}'
        self.data_paths = [os.path.join(self.data_dir, fname) for fname in os.listdir(self.data_dir)]

        self.translations = []

        for i, f in enumerate(self.data_paths):
            prf = Profiler()
            prf.load_csv(f, low_memory=False)
            tlr = OracleTranslator(tablename=self.filenames[i])
            self.translations.append(tlr(prf.profile))


    def test_agg_metadata(self):
        self.logger.info('Test: Agg Metadata')
        metadata = agg_translations(self.translations)
        self.logger.info(f'Metadata: \n {metadata}')

    
    def test_save_agg_metadata(self):
        self.logger.info('Test: Save Agg Metadata')
        fpath = os.path.join(os.getcwd(), 'testmeta.json')
        agg_translations(self.translations, filepath=fpath)

        self.assertTrue(os.path.isfile(fpath))

        cleanup
        os.remove(fpath)


    # def test_create_temp_dir(self):
    #     pass 

    
    # def test_create_archive(self):
    #     pass


if __name__ == "__main__":
    unittest.main()