# Задача 30:  
#               Заполните массив элементами арифметической прогрессии. Её первый элемент,
#               разность и количество элементов нужно ввести с клавиатуры. Формула для получения
#               n-го члена прогрессии: an = a1 + (n-1) * d.
#               Каждое число вводится с новой строки.


a1 = int(input('Введите первый элемент арифметической прогрессии : '))
d = int(input('Введите разность арифметической прогрессии: '))
n = int(input('Введите количество элементов прогрессии для вывода на печать: '))
list_1=[a1]
for i in range(2,n+1):
    if i<=n+1:
       an=a1+(i-1)*d
       list_1.append(an)
print(list_1)
