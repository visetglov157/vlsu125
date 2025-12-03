num = input('Введите строку: ')
x = set('0123456789')
count = 0
# перебор строки по символам
for char in num:
    if char in x:
        count += 1
print(f'Количество цифр в строке: {count}')