<<<<<<< Updated upstream
import unittest


class TestSum(unittest.TestCase): #TestSum inherits unittest.TestCase

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6") #test list

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6") #test tuple; negative control (won't work)

if __name__ == '__main__':
=======
import unittest


class TestSum(unittest.TestCase): #TestSum inherits unittest.TestCase

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6") #test list

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6") #test tuple; negative control (won't work)

if __name__ == '__main__':
>>>>>>> Stashed changes
    unittest.main()