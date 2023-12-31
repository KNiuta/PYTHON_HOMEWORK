# Задача 24:

# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
# причем кусты высажены только по окружности. Таким образом, у каждого куста
# есть ровно два соседних. Всего на грядке растет N кустов. 
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора
# на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.

# Напишите программу для нахождения максимального числа ягод, которое может 
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

import random
num = int(input("введите количество кустов: "))
list_1 = list(random.randint(0, 10) for i in range(num))
print(f'количество ягод на кустах {list_1}')

list_2 = []
i = 0
sum = 0

if (i < num - 1):
        sum = list_1[i] + list_1[i - 1] + list_1[i + 1]
        i += 1
else:
        sum = list_1[i] + list_1[i - 1] + list_1[0]
list_2.append(sum)
list_2.sort()

print(f"максимальное число ягод за одну итерацию {list_2[-1]}")