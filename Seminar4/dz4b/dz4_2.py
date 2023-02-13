# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

lst1 = []
lst2 = []

for i in range(12):
    l1 = random.randint(1, 12)
    lst1.append(l1)

for j in range(len(lst1)):
    if lst1[j] not in lst2:
        lst2.append(lst1[j])

print(lst1)
print(lst2)