# test_profile.py


import unittest
import os
import logging

# Config
from tests import config, setup


class TestProfilerActions(unittest.TestCase):
    
    def setUp(self):
        setup(log=True)
        self.logger = logging.getLogger(__name__)


    def test_profiler_load(self):
        self.logger.info('Test: Profiler Load')
        pass