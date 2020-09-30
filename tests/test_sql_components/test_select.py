# test_archivor.py


import unittest
import os
import logging

# Config
from tests import config, setup

# User Libs
from sql import Query


data_dir = os.path.join(os.getcwd(),'tests', 'data')


class TestQuery(unittest.TestCase):
    
    def setUp(self):
        setup(log=True)
        self.logger = logging.getLogger(__name__)

    def test_select(self):
        q = Query()
        q.Select('test_table.something', 'something_else')
        self.assertIsNotNone(q)
        self.logger.info(f"Select Statement Created: \n{q}")

    def test_from(self):
        q = Query()
        q.From('test_table')
        self.assertIsNotNone(q)
        self.logger.info(f"From Statement Created: \n{q}")

    def test_select_from(self):
        q = Query()
        q.Select('Item1', 'Item2').From('TestTable')
        self.logger.info(f"Query Statement Created: \n{q}")



if __name__ == "__main__":
    unittest.main()