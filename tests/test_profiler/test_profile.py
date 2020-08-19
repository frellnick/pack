# test_profile.py


import unittest
import os
import logging

# Config
from tests import config, setup

# User Libs
from profile import Profiler


class TestProfilerActions(unittest.TestCase):
    
    def setUp(self):
        setup(log=True)
        self.logger = logging.getLogger(__name__)

        self.data_dir = os.path.join(os.getcwd(),'tests', 'data')
        assert len(os.listdir(self.data_dir)) > 0, f'Data files missing from data directory {self.data_dir}'
        self.data_paths = [os.path.join(self.data_dir, fname) for fname in os.listdir(self.data_dir)]


    def test_profiler_load(self):
        self.logger.info('Test: Profiler Load')
        profilers = []
        for f in self.data_paths:
            prf = Profiler()
            prf.load_csv(f, low_memory=False)
            profilers.append(prf)

        for p in profilers:
            self.assertEqual(len(p.data), 3)

    
    def test_profiler_gen(self):
        self.logger.info('Test: Profiler Gen')
        profilers = []
        for f in self.data_paths:
            prf = Profiler()
            prf.load_csv(f, low_memory=False)
            profilers.append(prf)

        profiles = []
        for p in profilers:
            profile = p.profile
            profiles.append(profile)

        self.logger.info(f'Generated profiles: {profiles}')







if __name__ == "__main__":
    unittest.main()