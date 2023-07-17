# Задача 32: 
#          Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
#          (т.е. не меньше заданного минимума и не больше заданного максимума)



import random

list_1=[random.randint(0, 10) for i in range(10)]
print(list_1)
min=int(input("Минимальное значение : "))
max=int(input("Максимальное значение "))
List_2=[]

if max>=min:
   for i in range(len(list_1)):
      if max>=list_1[i] and min<=list_1[i]:
          List_2.append(i)
print("Количество элементов:",len(List_2))
print("Индексы:",List_2)