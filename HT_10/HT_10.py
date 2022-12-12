'''напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент,
в исходном списке минимум 2 элемента '''
# def change(lst):
#     if len(lst) < 2:
#         print("enter at least 2 numbers")
#     else:
#         a = lst[0]
#         b = lst[-1]
#         lst = [b,a]
#         return print(lst)
#
# change(lst=[1,2,3,5,47,7])

#  TASK 2
'''Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь, 
в котором каждый элемент списка является и ключом и значением.
Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.'''
# def to_dict(lst):
#     if not isinstance(lst, (list)):
#         return print("not a list")
#     dict = {el: el for el in lst}
#     return print(dict)
#
# to_dict(lst=[2,3,5,4])
# to_dict(lst=["First", 2, "new"])

# TASK 3
'''Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start» до величины «end» включительно.
 Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.'''
#def sum_range(start,end):
#     summ = 0
#     if start > end:
#         for i in range(end, start + 1):
#             summ += i
#         print(summ)
#     else:
#         for i in range(start, end+1):
#             summ += i
#         print(summ)
#
# sum_range(0,100)
# sum_range(10,0)

# TASK 4
'''
Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать построчно последние строки 
в количестве lines (на всякий случай проверим, что задано положительное целое число). '''

# def read_last(lines, file):
#     if not isinstance(lines,(int)) and lines < 0:
#         return print("Error, enter digit please")
#     elif not isinstance(file, str):
#         print("Wrong file name")
#
#     with open(file, "r") as f:
#         print(*f.readlines()[-lines:])
#
# read_last(20,"example.txt")

