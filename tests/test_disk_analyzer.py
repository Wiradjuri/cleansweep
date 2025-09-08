import os
import unittest
from src.cleaners.disk_analyzer import DiskAnalyzer

class TestDiskAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = DiskAnalyzer()

    def test_list_largest_files(self):
        # Create a temporary directory and files for testing
        test_dir = 'test_directory'
        os.makedirs(test_dir, exist_ok=True)
        file_sizes = [1024, 2048, 512, 4096]  # Sizes in bytes
        file_names = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt']

        for name, size in zip(file_names, file_sizes):
            with open(os.path.join(test_dir, name), 'wb') as f:
                f.write(os.urandom(size))

        # Test the listing of largest files
        largest_files = self.analyzer.list_largest_files(test_dir, N=2)
        expected_files = sorted(file_names, key=lambda x: os.path.getsize(os.path.join(test_dir, x)), reverse=True)[:2]

        self.assertEqual([f[0] for f in largest_files], expected_files)

    def tearDown(self):
        # Clean up the temporary directory and files
        test_dir = 'test_directory'
        for file in os.listdir(test_dir):
            os.remove(os.path.join(test_dir, file))
        os.rmdir(test_dir)

if __name__ == '__main__':
    unittest.main()