# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1
n = int(input('Введите натуральное число n: '))
x = int(input('Введите число x: '))
lst = list(range(1, n + 1))
count = 0
for i in lst:
    if lst[i - 1] == x:
        count += 1
if count > 0:
    print(f'Число {x} встречается в списке lst {count} раз ')
else:
    print(f'В списке нет числа {x} ')



# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

n = int(input('Введите натуральное число n: '))
x = int(input('Введите  число x: '))
lst = range(1, n + 1)
min_r = x - lst[0]
index = 0
for i in range(1, n):
    count = (x - lst[i])
    if count < min_r:
        min_r = count
        index = i
print(f'Число {lst[index]} самый близкий по величне элемент к {x}')


# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать,
# что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# # *Пример:*
# # ноутбук
#     12
dictionary_en = {1:"AEIOULNSTR", 2:"DG", 3:"BCMP", 4:"FHVWY", 5:"K", 8:"J, X", 10:"QZ"}
dictionary_ru = {1:"АВЕИНОРСТ", 2:"ДКЛМПУ", 3:"БГЁЬЯ", 4:"ЙЫ", 5:"ЖЗХЦЧ", 8:"ШЭЮ", 10:"ФЩЪ"}
a = input("Введите слово на английском или русском языке ").upper()
summ = 0
for i in a:
    for k, v in dictionary_ru.items():
        if i in v:
            summ += k
    for j, s in dictionary_en.items():
        if i in s:
            summ += j
print(f"Стоимость слова {a} = {summ}")