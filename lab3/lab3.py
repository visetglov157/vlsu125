def find_max_distance():
    try:
        # Чтение количества зданий
        n = int(input().strip())
        
        # Проверка на минимальное количество зданий
        if n <= 0:
            raise ValueError("Количество зданий должно быть положительным числом")
        
        # Чтение типов зданий
        buildings_input = input().strip()
        if not buildings_input:
            raise ValueError("Вторая строка не может быть пустой")
            
        buildings = list(map(int, buildings_input.split()))
        # len - возвращает кол-во элементов в объекте
        # Проверка соответствия количества зданий
        if len(buildings) != n:
            raise ValueError(f"Ожидалось {n} зданий, но получено {len(buildings)}")
        
        # Проверка допустимых значений
        for building in buildings:
            if building not in [0, 1, 2]:
                raise ValueError(f"Недопустимый тип здания: {building}. Допустимы только 0, 1, 2")
        
        # Проверка наличия хотя бы одного дома и магазина
        if 1 not in buildings:
            raise ValueError("На проспекте должен быть хотя бы один жилой дом")
        if 2 not in buildings:
            raise ValueError("На проспекте должен быть хотя бы один магазин")
        
        # Поиск позиций магазинов
        shops = []
        for i in range(n):
            if buildings[i] == 2:
                shops.append(i)
        
        max_distance = 0
        
        # Для каждого жилого дома находим расстояние до ближайшего магазина
        for i in range(n):
            if buildings[i] == 1:
                min_dist = float('inf')
                
                # Ищем ближайший магазин
                for shop in shops:
                    distance = abs(i - shop)
                    if distance < min_dist:
                        min_dist = distance
                
                # Обновляем максимальное расстояние
                if min_dist > max_distance:
                    max_distance = min_dist
        
        return max_distance
        
    except ValueError as e:
        print(f"Ошибка ввода данных: {e}")
        return None
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return None

# Основная программа
def main():
    try:
        result = find_max_distance()
        if result is not None:
            print("Результат -", result)
    except Exception:
        print("Программа завершена с ошибкой")

# Запуск программы
if __name__ == "__main__":
    main()