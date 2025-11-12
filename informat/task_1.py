# создание функции для решения задачи
def check_identifier(input_str):
    if not input_str:
        return False
# создание множеств символов
    lett = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_')
    num = set('0123456789')
    allowed_chars = lett | num # объединение множеств
    flag = True
# проверка первого символа(доступны только буквы и знак подчеркивания)
    if input_str[0] not in lett:
        flag = False
# проверка остальных символов
    else:
        for char in input_str[1:]:
            if char not in allowed_chars:
                flag = False
                break
    return flag
def main():
    input_str = input('Введите строку для проверки: ')
# проверка
    if check_identifier(input_str):
        print('Строка корректна')
    else:
        print('Строка некорректна')

if __name__ == "__main__":
    main()