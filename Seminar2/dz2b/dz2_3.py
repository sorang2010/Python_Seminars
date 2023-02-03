# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input("Введите число элементов списка: "))

lst = [i for i in range(-n, n + 1)]
print(f"список из N элементов, заполненных числами из промежутка [-N, N]: {lst}")

output1 = open('file.txt', 'r')
data1 = output1.read()
output1.close()

ll = data1.split("\n")
ld = []

for i in ll:
    j = int(i)
    ld.append(j)
# print(ld)

multi = lst[ld[0]] * lst[ld[1]]
print(multi)
