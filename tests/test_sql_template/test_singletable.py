# test_archivor.py


import unittest
import os
import logging

# Config
from tests import config, setup

# User Libs
from sql import SingleTableTest


data_dir = os.path.join(os.getcwd(),'tests', 'data')


class TestSingleTableTestCreation(unittest.TestCase):
    
    def setUp(self):
        setup(log=True)
        self.logger = logging.getLogger(__name__)

    def test_create_singletabletest(self):
        s = SingleTableTest(
            tablename='test_table',
            data=None)
        self.assertIsNotNone(s)

        self.logger.info(f"Created Test Query:\n{s.assemble()}")


    def test_singletabletest_with_data(self):
        data = {
            'expected_mpi':1000,
            'expected_id':1000,
            'record_count':1000,
        }
        s = SingleTableTest(
            tablename='test_table_vs_exp',
            data=data,
        )
        self.assertIsNotNone(s)

        self.logger.info(f"Created Test Query:\n{s.assemble()}")


if __name__ == "__main__":
    unittest.main()