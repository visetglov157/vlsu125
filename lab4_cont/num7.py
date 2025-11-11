def count_characters(text):
    """Cловарь с количеством вхождений каждого символа"""
    try:
        char_count = {}
        for char in text:
            char_count[char] = char_count.get(char, 0) + 1
        return char_count
    except Exception as e:
        raise e

def main():
    """Основная функция с вводом/выводом"""
    try:
        text = input("Введите текст: ")
        result = count_characters(text)
        print(f"Текст: '{text}'")
        print(f"Словарь: {result}")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()