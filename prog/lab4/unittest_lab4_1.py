import unittest
import random
import lab4_1

class SimpleTestGenerateNumbers(unittest.TestCase):
    
    def test_basic_functionality(self):
        """Базовый тест работы функции"""
        # Вызываем функцию
        set1, set2, all_nums = lab4_1.generate_numbers_with_sets()
        
        # Проверяем основные требования
        self.assertEqual(len(set1), 5, "Первое множество должно содержать 5 чисел")
        self.assertEqual(len(set2), 10, "Второе множество должно содержать 10 чисел")
        self.assertEqual(len(all_nums), 15, "Общий список должен содержать 15 чисел")
        
        # Проверяем диапазоны
        for num in set1:
            self.assertTrue(1 <= num <= 10, f"Число {num} не в диапазоне 1-10")
        for num in set2:
            self.assertTrue(10 <= num <= 30, f"Число {num} не в диапазоне 10-30")

if __name__ == '__main__':
    unittest.main()