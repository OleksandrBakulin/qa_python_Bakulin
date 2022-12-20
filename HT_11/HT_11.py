'''
Написать декоратор call_times, который будет принимать в качестве параметра file_name,
считать количество вызовов функций и записывать в файл в формате f'{func_name} была вызвана {count} раза.\n'
Пример:
@call_times('foo.txt')
def foo():
  pass
@call_times('foo.txt')
def boo():
  pass
@call_times('calls.txt')
def doo():
  pass
foo()
boo()
foo()
foo()
boo()
doo()
Файл foo.txt:
foo была вызвана 3 раза
boo была вызвана 2 раза
Файл calls.txt:
doo была вызвана 1 раза
'''
from collections import defaultdict
counter = defaultdict(int)
def call_times(file_name):
    def decorator(func):
        def wrapper():
            counter[f"{file_name}_{func.__name__}"] += 1
            result = func()

            with open(file_name, 'w+') as f:
                for key, value in counter.items():
                    if key.startswith(file_name):
                        f.write(f'{key.split("_")[1]} was called {value} times.\n')
            return result
        return wrapper
    return decorator

@call_times('foo.txt')
def foo():
    pass
@call_times('foo.txt')
def boo():
    pass
@call_times('calls.txt')
def doo():
    pass

doo()
foo()
boo()
foo()
foo()
boo()
boo()