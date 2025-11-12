def create_odd_pairs():
    """Создает множество с нечетными числами парами"""
    try:
        result = set()
        for i in range(1, 20, 2):  # Нечетные числа от 1 до 19
            result.add(i)          # Первое нечетное число
            result.add(i + 2)      # Следующее нечетное число
        return result
    except Exception as e:
        print(f"Ошибка при создании множества: {e}")
        return set()
def main():
    """Основная функция"""
    try:
        odd_numbers = create_odd_pairs()
        print("Множество нечетных чисел:")
        print(odd_numbers)
        print(f"Количество чисел: {len(odd_numbers)}")
        print(f"Отсортированный список: {sorted(odd_numbers)}")
    except Exception as e:
        print(f"Ошибка в программе: {e}")
if __name__ == "__main__":
    main()