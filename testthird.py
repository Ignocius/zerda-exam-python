import unittest
from third import count_letter_in_string

class UnittestForThirdTask(unittest.TestCase):
    def test_if_normal_string_input_works(self):
        self.assertEqual(count_letter_in_string("apple","a"), 1)

    def test_if_upparcase_string_input_works(self):
        self.assertEqual(count_letter_in_string("Apple","a"), 1)

    def test_if_empty_input_works(self):
        self.assertEqual(count_letter_in_string("",""), 0)

    def test_if_empty_input_with_letter_works(self):
        self.assertEqual(count_letter_in_string("","l"), 0)

    def test_if_we_use_number_input(self):
        self.assertEqual(count_letter_in_string(123, 2), 0)

if __name__ == '__main__':
    unittest.main()
