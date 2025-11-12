import unittest
import num7

class TestCountCharacters(unittest.TestCase):

    def test_basic_case(self):
        """Тест базового случая"""
        result = num7.count_characters("ABBCAB")
        expected = {'A': 2, 'B': 3, 'C': 1}
        self.assertEqual(result, expected)

    def test_empty_string(self):
        """Тест пустой строки"""
        result = num7.count_characters("")
        expected = {}
        self.assertEqual(result, expected)

    def test_single_character(self):
        """Тест одного символа"""
        result = num7.count_characters("AAAAA")
        expected = {'A': 5}
        self.assertEqual(result, expected)

    def test_with_spaces(self):
        """Тест с пробелами"""
        result = num7.count_characters("hello world")
        expected = {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
        self.assertEqual(result, expected)

    def test_function_exists(self):
        """Тест что функция существует"""
        self.assertTrue(hasattr(num7, 'count_characters'))
        self.assertTrue(hasattr(num7, 'main'))

if __name__ == '__main__':
    unittest.main()