import os
import hashlib
import unittest
from src.cleaners.duplicate_finder import find_duplicates, remove_duplicates

class TestDuplicateFinder(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = 'test_dir'
        os.makedirs(self.test_dir, exist_ok=True)

        # Create test files
        self.file1 = os.path.join(self.test_dir, 'file1.txt')
        self.file2 = os.path.join(self.test_dir, 'file2.txt')
        self.file3 = os.path.join(self.test_dir, 'file3.txt')

        with open(self.file1, 'w') as f:
            f.write('This is a test file.')

        with open(self.file2, 'w') as f:
            f.write('This is a test file.')  # Duplicate of file1

        with open(self.file3, 'w') as f:
            f.write('This is another test file.')

    def tearDown(self):
        # Remove the test directory and its contents
        for file in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, file))
        os.rmdir(self.test_dir)

    def test_find_duplicates(self):
        duplicates = find_duplicates(self.test_dir)
        self.assertEqual(len(duplicates), 1)
        self.assertIn(self.file1, duplicates)
        self.assertIn(self.file2, duplicates)

    def test_remove_duplicates(self):
        remove_duplicates(self.test_dir)
        self.assertFalse(os.path.exists(self.file2))  # file2 should be removed
        self.assertTrue(os.path.exists(self.file1))    # file1 should still exist
        self.assertTrue(os.path.exists(self.file3))    # file3 should still exist

if __name__ == '__main__':
    unittest.main()