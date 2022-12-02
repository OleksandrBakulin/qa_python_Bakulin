''' UNCOMMENT CORRESPONDENT CODE TO CHECK IT '''
# # TASK 1
# my_list = []
# for i in range(5):
#     i += 1
#     a = int(input("enter digit here: "))
#     my_list.append(a)
# print(my_list)

# # TASK 2
'''
Дан список A = [1, 2, 3, 4, 5]
Удалить последнее число из списка
'''
# A = [1,2,3,4,5]
# A.remove(5)
# print(A)

# TASK 3
'''
Запросить у пользователя 10 чисел и записать их в список A
Запросить у пользователя число N
Вывести пользователю сколько в списке A повторяется число N
'''
# list = []
# for i in range(10):
#     i += 1
#     k = int(input("enter digit here: "))
#     list.append(k)
# N = int(input("Enter the digit to find: "))
# print(list.count(N))

# TASK 4
'''Запросить у пользователя число N
Запросить у пользователя N чисел и записать их в список A
Вывести список в обратной последовательности'''
# listed = []
# ask_digit = int(input("how many digits: "))
# for mulit in range(ask_digit):
#     mulit +=1
#     multi_enter = int(input("enter digit here: "))
#     listed.append(multi_enter)
# print(listed[::-1])

# TASK 5
'''Запросить у пользователя 5 чисел и записать их в список A
Записать все числа из списка A которые больше 5 в список C'''
# a_list = []
# c_list = []
# for i_count in range(5):
#     i_count += 1
#     new_input = int(input("enter digit here: "))
#     a_list.append(new_input)
# for a_list[0 +1] in a_list:
#         cou = a_list[+1]
#         if cou > 5:
#             c_list.append(cou)
# print(c_list)

#TASK 6
'''Запросить у пользователя число N
Запросить у пользователя N целых чисел и записать их в список A
Найти в нем минимальное и максимальное число с помощью цикла (запрещено использовать функцию min и max). Вывести эти числа.'''
# q_list = []
# t_input = int(input("how many ints ? : "))
# for l in range(t_input):
#     l +=1
#     o = int(input("enter digit here: "))
#     q_list.append(o)
# min_num = q_list[0]
# max_num = q_list[0]
# for i in q_list:
#     if i > max_num:
#         max_num = i
# for d in q_list:
#     if d < min_num:
#         min_num = d
# print(f'MAX: {max_num}, Min: {min_num}')

# TASK 7
'''Пользователь вводит текст нужно вывести количество чисел в этом тексте
Пример:
> 'Lorem 222 ipsum, 123 dolor 1 sit amet
Количество чисел: 3'''

# num_counter = 0
# user_input = input("enter your text here: ")
# for finder in user_input.split():
#     if finder.isdigit():
#         num_counter += 1
# print(f'here are {num_counter} numbers')