# Unit Tests for the find_longest_path.py

# Import required libraries
import unittest
import find_longest_path

class Testfind_longest_path(unittest.TestCase):
    def test_collect_graph(self):
        self.assertFalse(find_longest_path.collect_graph(open('test_1.txt', 'r')))
        self.assertFalse(find_longest_path.collect_graph(open('test_2.txt', 'r')))
        self.assertFalse(find_longest_path.collect_graph(open('test_3.txt', 'r')))
        self.assertFalse(find_longest_path.collect_graph(open('test_4.txt', 'r')))
        self.assertFalse(find_longest_path.collect_graph(open('test_5.txt', 'r')))
        self.assertFalse(find_longest_path.collect_graph(open('test_6.txt', 'r')))

        self.assertTrue(find_longest_path.collect_graph(open('inSample_1.txt', 'r')))
        self.assertTrue(find_longest_path.collect_graph(open('inSample_2.txt', 'r')))
        self.assertTrue(find_longest_path.collect_graph(open('inSample_3.txt', 'r')))
        self.assertTrue(find_longest_path.collect_graph(open('inSample_4.txt', 'r')))


if __name__ == '__main__':
    unittest.main()

