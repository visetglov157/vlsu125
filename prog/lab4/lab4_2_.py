def find_common_digits():
    try:
        num1 = int(input("Введите первое целое число: "))
        num2 = int(input("Введите второе целое число: "))
    except ValueError:
        print("Ошибка! Введите целые числа.")
        return
    set1 = set(str(abs(num1)))  # abs() для работы с отрицательными числами
    set2 = set(str(abs(num2)))
    # Для нахождения пересечения
    common = set1 & set2
    print(f"Анализ чисел {num1} и {num2}:")
    print(f"Цифры в числе {num1}: {sorted(set1)}")
    print(f"Цифры в числе {num2}: {sorted(set2)}")
    
    if common:
        print(f"Общие цифры: {sorted(common)}")
    else:
        print("Общих цифр нет")
find_common_digits()