import os
import sys
import json

# # TASK 4
# my_dict = {'one': '1', 'two': '2', 'three': '3'}
# new_dict = {value: key for key, value in my_dict.items()}
# print(new_dict)

# TASK 4
# f = open("example.txt", "x")
# f.writelines(f'{new_dict}')
# f.close()
#
# TASK 6
# def renamer():
#     name = sys.platform
#     if "linux" == name:
#         os.system("mv test.txt linux.txt")
#     if "mac" == name:
#         os.system("mv test.txt mac.txt")
#     if "win32" == name:
#         os.system("mv test.txt windows.txt")
# renamer()

## TASK 7
# def generator(from_: int,to_: int):
#     while from_ < to_:
#         yield from_
#         from_ += 1
#
# a = int(input("Enter first: "))
# b = int(input("Enter second: "))
#
# gen = generator(a,b)
# while a <= b:
#     print(next(gen))

# TASK 8
# class A:
#     name = "A"
#     def __init__(self,):
#         self.name = "A"
#
# class B(A):
#     name = "B"
#
# class C(B):
#     name = "C"
#     def __init__(self):
#         super().__init__()
#
# print(A.name)
# print(B.name)
# print(C.name)
# print(C().name)

# TASK 9
# args - це позиційний аргумент, записуєтся у вигляді кортежу,
#  kwargs - це агрументи які передаюися у вигляді ключа та значення, та зберігаются у вигляді словника

# def task_nine(*args, **kwargs):
#     a = args
#     print(a)
#     b = kwargs
#     print(b)
#
# task_nine(1,2,3, alex=1, phone=2,neka="morgondagen")
#
# TASK 10
# def json_field(file_path, key, value):
#     with open(file_path, 'r') as file:
#         data = json.load(file)
#         data[key] = value
#     with open(file_path, 'w') as file:
#         json.dump(data, file, indent=4)
# json_field("jsonfile.json",key="author",value="nes")