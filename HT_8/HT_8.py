#TASK 1
'''Дано два множества A и B
В множестве А находятся имена должников за Сентябрь
В множестве B находятся имена должников за Октябрь
Найти:
* Вывести имена людей которые должны за Сентябрь и Октябрь
* Вывести должников за Октябрь у которых нет долга за Сентябрь'''

# A = {"Alex", "Andrew", "Ihor", "Oleg", "Petr", "Ivan"}
# B = {"Egor", "Olga", "Andrew","Igor", "Evgen", "Dmytro", "Oleg"}
#
# print(f'Имена людей которые должны за Сентябрь и Октябрь {A.intersection(B)}')
# print(f'Имена должников за Октябрь у которых нет долга за Сентябрь{B.difference(A)}')

#TASK 2
'''Права доступа
Вирус повредил систему прав доступа к файлам. Известно, что над каждым файлом можно производить определенные действия:
запись – W;
чтение – R;
запуск – X.
На вход программе подается:
число n – количество файлов;
n строк с именами файлов и допустимыми операциями;
число m – количество запросов к файлам;
m запросов вида «операция файл».
Для каждого допустимого запроса программа должна возвращать OK, для недопустимого – Access denied.
Пример ввода:
3
python.exe X
book.txt R W
notebook.exe R W X
5
read python.exe
read book.txt
write notebook.exe
execute notebook.exe
write book.txt
Пример вывода:
Access denied
OK
OK
OK
OK'''
access_cond = {'W': 'write', 'R': 'read', 'X': 'execute'}
permission = {}
for i in range(int(input("How many files: "))):
    try:
        x = input("Enter name of file (test.txt) and action (R W X) : ").split()
        permission[x[0]] = [access_cond[i] for i in x[1:]]
    except KeyError:
        print("Error, please enter as in example 'file.txt R W X'")

for i in range(int(input("Enter amount of actions on files: "))):
        diff, n = input(f"Enter action({access_cond.values()}) and file name ({permission.keys()}): ").split()
        print('OK' if diff in permission[n] else 'Access denied')
'''Сюда нужно кучу всяких защит от неправильных значений
но дописывать их уже некогда (((( 
'''