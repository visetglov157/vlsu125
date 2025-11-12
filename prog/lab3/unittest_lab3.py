import unittest
import lab3

class TestBuildingDistance(unittest.TestCase):

    def test_normal_case_1(self):
        """Тест: магазин между домами"""
        import builtins
        original_input = builtins.input
        
        test_inputs = ["3", "1 2 1"]
        builtins.input = lambda: test_inputs.pop(0)
        
        result = lab3.find_max_distance()
        self.assertEqual(result, 1)
        builtins.input = original_input

    def test_normal_case_2(self):
        """Тест: дом в начале, магазин в конце"""
        import builtins
        original_input = builtins.input
        
        test_inputs = ["5", "1 0 0 0 2"]
        builtins.input = lambda: test_inputs.pop(0)
        
        result = lab3.find_max_distance()
        self.assertEqual(result, 4)
        builtins.input = original_input

    def test_normal_case_3(self):
        """Тест: магазин в начале, дом в конце"""
        import builtins
        original_input = builtins.input
        
        test_inputs = ["5", "2 0 0 0 1"]
        builtins.input = lambda: test_inputs.pop(0)
        
        result = lab3.find_max_distance()
        self.assertEqual(result, 4)
        builtins.input = original_input

    def test_complex_case(self):
        """Тест: сложный случай"""
        import builtins
        original_input = builtins.input
        
        test_inputs = ["10", "1 0 0 0 2 0 1 0 2 1"]
        builtins.input = lambda: test_inputs.pop(0)
        
        result = lab3.find_max_distance()
        self.assertEqual(result, 4)
        builtins.input = original_input

    def test_multiple_shops(self):
        """Тест: несколько магазинов"""
        import builtins
        original_input = builtins.input
        
        test_inputs = ["6", "2 1 0 1 0 2"]
        builtins.input = lambda: test_inputs.pop(0)
        
        result = lab3.find_max_distance()
        self.assertEqual(result, 2)
        builtins.input = original_input

    def test_far_distance(self):
        """Тест: дом далеко от магазина"""
        import builtins
        original_input = builtins.input
        
        test_inputs = ["7", "1 0 1 0 1 0 2"]
        builtins.input = lambda: test_inputs.pop(0)
        
        result = lab3.find_max_distance()
        self.assertEqual(result, 6)
        builtins.input = original_input

    def test_minimal_case(self):
        """Тест: минимальное количество зданий"""
        import builtins
        original_input = builtins.input
        
        test_inputs = ["2", "1 2"]
        builtins.input = lambda: test_inputs.pop(0)
        
        result = lab3.find_max_distance()
        self.assertEqual(result, 1)
        builtins.input = original_input

    def test_house_between_shops(self):
        """Тест: дом между двумя магазинами - ИСПРАВЛЕННЫЙ ТЕСТ"""
        import builtins
        original_input = builtins.input
        
        test_inputs = ["3", "2 1 2"]
        builtins.input = lambda: test_inputs.pop(0)
        
        result = lab3.find_max_distance()
        self.assertEqual(result, 1)
        builtins.input = original_input

    def test_single_house_far(self):
        """Тест: один дом далеко от магазина"""
        import builtins
        original_input = builtins.input
        
        test_inputs = ["5", "2 0 0 0 1"]
        builtins.input = lambda: test_inputs.pop(0)
        
        result = lab3.find_max_distance()
        self.assertEqual(result, 4)
        builtins.input = original_input

    def test_invalid_number_format(self):
        """Тест: нечисловой формат для N"""
        import builtins
        original_input = builtins.input
        
        test_inputs = ["abc", "1 2"]
        builtins.input = lambda: test_inputs.pop(0)
        
        result = lab3.find_max_distance()
        self.assertIsNone(result)
        builtins.input = original_input

    def test_negative_buildings(self):
        """Тест: отрицательное количество зданий"""
        import builtins
        original_input = builtins.input
        
        test_inputs = ["-5", "1 2"]
        builtins.input = lambda: test_inputs.pop(0)
        
        result = lab3.find_max_distance()
        self.assertIsNone(result)
        builtins.input = original_input

    def test_zero_buildings(self):
        """Тест: ноль зданий"""
        import builtins
        original_input = builtins.input
        
        test_inputs = ["0", "1 2"]
        builtins.input = lambda: test_inputs.pop(0)
        
        result = lab3.find_max_distance()
        self.assertIsNone(result)
        builtins.input = original_input

    def test_empty_second_line(self):
        """Тест: пустая вторая строка"""
        import builtins
        original_input = builtins.input
        
        test_inputs = ["3", ""]
        builtins.input = lambda: test_inputs.pop(0)
        
        result = lab3.find_max_distance()
        self.assertIsNone(result)
        builtins.input = original_input

    def test_building_count_mismatch(self):
        """Тест: несоответствие количества зданий"""
        import builtins
        original_input = builtins.input
        
        test_inputs = ["5", "1 2 3"]
        builtins.input = lambda: test_inputs.pop(0)
        
        result = lab3.find_max_distance()
        self.assertIsNone(result)
        builtins.input = original_input

    def test_invalid_building_type(self):
        """Тест: недопустимый тип здания"""
        import builtins
        original_input = builtins.input
        
        test_inputs = ["3", "1 5 2"]
        builtins.input = lambda: test_inputs.pop(0)
        
        result = lab3.find_max_distance()
        self.assertIsNone(result)
        builtins.input = original_input

if __name__ == '__main__':
    unittest.main()