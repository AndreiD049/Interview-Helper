import unittest
import os
import source.validators as v
import source.utils as u

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.path = os.path.join(os.path.split(__file__)[0], "assets", "utils")

    def test_random_files(self):
        self.assertEquals(len(u.select_n_random_files(1, os.path.join(self.path, "empty_folder"), "json")), 0)
        self.assertIsInstance(u.select_n_random_files(1, os.path.join(self.path, "empty_folder"), "json"), list)
        self.assertEquals(len(u.select_n_random_files(3, os.path.join(self.path, "folder"), "json")), 3)
        self.assertLess(len(u.select_n_random_files(30, os.path.join(self.path, "folder"), "json")), 30)
        
    def test_random_valid_files(self):
        self.assertEquals(len(u.select_n_valid_files(v.ValidatorErrorChecking.validate, 2, os.path.join(self.path, "folder"), "json")), 2)