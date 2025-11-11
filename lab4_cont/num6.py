def create_reverse_dict_from_number(n):
    try:
        if n < 0:
            raise ValueError("Число должно быть неотрицательным!")
        
        numbers = list(range(1, n + 1))
        reverse_dict = {key: n - key + 1 for key in numbers}
        return numbers, reverse_dict
        
    except Exception as e:
        raise e
def main():
    """Основная функция с вводом/выводом"""
    try:
        n = int(input("Введите целое неотрицательное число: "))
        numbers, reverse_dict = create_reverse_dict_from_number(n)
        print(f"Список: {numbers}")
        print(f"Словарь: {reverse_dict}")
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
if __name__ == "__main__":
    main()