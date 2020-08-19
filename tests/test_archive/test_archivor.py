# test_archivor.py


import unittest
import os
import logging

# Config
from tests import config, setup

# User Libs
from profile import Profiler
from translator import OracleTranslator
from archivor import agg_translations, create_temp, copy_files, clean_temp, create_archive


data_dir = os.path.join(os.getcwd(),'tests', 'data')


class TestArchivorActions(unittest.TestCase):
    
    def setUp(self):
        setup(log=True)
        self.logger = logging.getLogger(__name__)

        self.filenames = os.listdir(data_dir)
        assert len(os.listdir(data_dir)) > 0, f'Data files missing from data directory {data_dir}'
        self.data_paths = [os.path.join(data_dir, fname) for fname in os.listdir(data_dir)]

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

        # cleanup
        os.remove(fpath)


    def test_create_temp_dir(self):
        self.logger.info('Test: Create Temporary Directory')
        temppath = create_temp(data_dir)
        self.assertTrue(os.path.isdir(temppath))
        self.logger.info(f'Created directory {temppath}')

        # cleanup
        clean_temp(temppath)
        

    def test_copy_files(self):
        self.logger.info('Test: Copy Files')
        temppath = create_temp(data_dir)
        copy_files(data_dir, temppath)

        self.assertEqual(len(os.listdir(data_dir)), len(os.listdir(temppath)))

        # cleanup
        clean_temp(temppath)
    

    def test_create_archive(self):
        self.logger.info('Test: create_archive')
        zippath = create_archive(translations=self.translations, dirpath=data_dir, zipname='PARTNER_TESTFILE.zip')
        
        self.assertTrue(os.path.isfile(zippath))

        #cleanup
        os.remove(zippath)


if __name__ == "__main__":
    unittest.main()