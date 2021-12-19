import unittest
import sys, os

from unittest.mock import patch

sys.path.append(os.getcwd())
from main import *

class TestGetRoots(unittest.TestCase):
    def test_get_roots_returns_integer(self):
        self.assertIsInstance(get_roots(-2, 4, 3), list)
        self.assertIsInstance(get_roots(1, 2, 3), list)
        self.assertIsInstance(get_roots(10, -7, 32), list)

    def test_get_roots(self):
        self.assertEqual(get_roots(-2, 4, 3), [-0.58, 2.58])
        self.assertEqual(get_roots(1, 2, 3), [])
        self.assertEqual(get_roots(10, 7, -32), [1.47, -2.17])

if __name__ == "__main__":
    unittest.main()