def calculate_numbers():
    """Вычисляет числа от 1 до 50, которые делятся на 3 или на 4, но не на оба"""
    try:
        result = set()
        for num in range(1, 51):
            div_by_3 = num % 3 == 0
            div_by_4 = num % 4 == 0
            # Делится на 3 ИЛИ на 4, но НЕ на оба
            if (div_by_3 or div_by_4) and not (div_by_3 and div_by_4):
                #Добавление полученного числа во множество
                result.add(num)
        return result
    except Exception as e:
        print(f"Ошибка при вычислении: {e}")
        return set()
def main():
    """Основная функция"""
    try:
        numbers = calculate_numbers()
        print("Числа от 1 до 50, которые делятся на 3 или на 4, но не на оба:")
        print(f"Всего найдено: {len(numbers)} чисел")
        print(f"Список: {sorted(numbers)}")
    except Exception as e:
        print(f"Ошибка в программе: {e}")

if __name__ == "__main__":
    main()