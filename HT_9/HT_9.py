import random
# # TASK 1
# #Дан файл с произвольным текстом, необходимо найти все числа в файле и записать в список numbers
# a = open("task1.txt", 'r')
# numbers = []
# file = a.read()
# for finder in file.split():
#     if finder.isdigit():
#         numbers.append(finder)
# print(numbers)
# file = a.close()
# # TASK 2
# #Запросить у пользователя текст и записать его в файл data.txt
# text_inp = input("Enter text here: ")
# new_file = open('data.txt', "w")
# new_file.write(f'{text_inp}')
# new_file.close()

# TASK 3
#Запросить у пользователя число N и запросить N чисел у пользователя, потом записать их в файл numbers.txt через пробел
# task_three = open('numbers.txt', 'w')
# ask_digit = int(input("how many digits: "))
# for multi in range(ask_digit):
#     multi_enter = int(input("enter digit here: "))
#     task_three.writelines(f'{multi_enter} ')
# task_three.close()

# TASK 4
# Сгенерировать 100 рандомных чисел и записать их в файл random_numbers.txt, где одна строка = одно число
# rnd = [random.randint(0, 100) for _ in range(100)]
# random_numbers = open("random_numbers.txt", 'w')
# for i in rnd:
#     random_numbers.write(f'{i}\n')
#
# Задание 5
# Дан файл с произвольным текстом, нужно найти количество слов в файле и вывести пользователю
# rnd_text = open("random_text.txt", 'r')
# a = 0
# file_read = rnd_text.read()
# for count in file_read.split():
#     a +=1
# print(f'in this text {a} words')

# Задание 6
# Дан файл в котором записаны числа через пробел, необходимо вывести пользователю сумму этих чисел
# task_numbers = open("task_6.txt", 'r')
# a = 0
# b = task_numbers.read()
# for _ in list(map(int, b.split())):
#     a = _ + a
# print(f'the sum is: {a}')

# Задание 7
# Дан файл в котором записан текст, необходимо вывести топ 5 строк которые чаще всего повторяются, пример:
# 'в' - 20 раз, 'привет' - 10 раз, 'как' - 9 раз, 'у' - 7  'world' - 4
'''NOT OPTIMIZED'''
a = open("task7.txt", 'r')
b = a.read()
i = 0
first = 0
second = 0
third = 0
fourth = 0
fifth = 0
count_list = {i: b.count(i) for i in b.split()}
for i in count_list.values():
    if i >= first:
       first = i
    elif i >= second:
        second = i
    elif i >= third:
        third = i
    elif i >= fourth:
        fourth = i
    elif i >= fifth:
        fifth = i
print(f'"{list(count_list.keys())[list(count_list.values()).index(first)]}" appears {first} times')
print(f'"{list(count_list.keys())[list(count_list.values()).index(second)]}" appears {second} times')
print(f'"{list(count_list.keys())[list(count_list.values()).index(third)]}" appears {third} times')
print(f'"{list(count_list.keys())[list(count_list.values()).index(fourth)]}" appears {fourth} times')
print(f'"{list(count_list.keys())[list(count_list.values()).index(fifth)]}" appears {fifth} times')


