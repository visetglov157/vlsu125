import unittest
import num6

class TestCreateReverseDict(unittest.TestCase):

    def test_valid_input(self):
        numbers, result = num6.create_reverse_dict_from_number(3)
        self.assertEqual(numbers, [1, 2, 3])
        self.assertEqual(result, {1: 3, 2: 2, 3: 1})
        
    def test_zero_input(self):
        numbers, result = num6.create_reverse_dict_from_number(0)
        self.assertEqual(numbers, [])
        self.assertEqual(result, {})

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            num6.create_reverse_dict_from_number(-5)
if __name__ == '__main__':
    unittest.main()