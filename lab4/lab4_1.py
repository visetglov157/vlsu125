import random

def generate_numbers_with_sets():
    set_1_to_10 = set()
    set_10_to_30 = set()
    while len(set_1_to_10) < 5:
        set_1_to_10.add(random.randint(1, 10))
    while len(set_10_to_30) < 10:
        set_10_to_30.add(random.randint(10, 30))
    numbers_1_to_10 = list(set_1_to_10)
    numbers_10_to_30 = list(set_10_to_30)
    all_numbers = numbers_1_to_10 + numbers_10_to_30
    
    # Вывод результатов
    print("5 уникальных чисел от 1 до 10:", numbers_1_to_10)
    print("10 уникальных чисел от 10 до 30:", numbers_10_to_30)
    print("Все 15 уникальных чисел:", all_numbers)
    print(f"Общее количество: {len(all_numbers)}")
    
    return set_1_to_10, set_10_to_30, all_numbers
set1, set2, all_nums = generate_numbers_with_sets()
