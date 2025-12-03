chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
#Ввод данных
text = input('Введите ФИО и дату рождения: ')
nchar = False
#Перебор символов строки 
for char in text:
    if char not in char:
        nchar = True
        #прерывание цикла, так как есть посторонний символ
        break
if nchar:
    print('Присутствует посторонний символ')
else:
    print("В строке нет посторонних символов")

print(text)