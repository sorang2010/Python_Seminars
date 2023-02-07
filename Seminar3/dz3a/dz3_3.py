# Задача из презентации семинара
# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
'''
● A, E, I, O, U, L, N, S, T, R – 1 очко;
● D, G – 2 очка;
● B, C, M, P – 3 очка;
● F, H, V, W, Y – 4 очка;
● K – 5 очков;
● J, X – 8 очков;
● Q, Z – 10 очков.
А русские буквы оцениваются так:
● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
● Д, К, Л, М, П, У – 2 очка;
● Б, Г, Ё, Ь, Я – 3 очка;
● Й, Ы – 4 очка;
● Ж, З, Х, Ц, Ч – 5 очков;
● Ш, Э, Ю – 8 очков;
● Ф, Щ, Ъ – 10 очков.
'''
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

str = 'ноутбукф'
print(f"слово а вход: {str}")
scr_eng = {1:'AaEeIiOoUuLlNnSsTtRr', 2:'DdGg', 3:'BbCcMmPp', 4:'FfHhVvWwYy', 5:'Kk', 8:'JjXx', 10:'QqZz'}
scr_ru = {1:'АаВвЕеИиНнОоРрСсТт', 2:'ДдКкЛлМмПпУу', 3:'БбГгЁёЬьЯя', 4:'ЙйЫы', 5:'ЖжЗзХхЦцЧч', 8:'ШшЭэЮю', 10:'ФфЩщЪъ'}

summ1 = 0

for i in str:
    for j in scr_eng.keys():
        if i in scr_eng[j]:
            # print(j)
            summ1 += j
    for j in scr_ru.keys():
        if i in scr_ru[j]:
            # print(j)
            summ1 += j
print(f"стоимость введенного пользователем слова: {summ1}")