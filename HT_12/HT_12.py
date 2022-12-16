'''Написать функцию которая принимает целое число - number. Функция должна возвращать 'yes' если number является степенью двойки,
иначе 'no'. Запрещено пользоваться функцией или оператором возведение в степень.
Пример:
is_power_of_two(256) # 'yes' потому что 2 в 8 степени это 256
is_power_of_two(125) # 'no' потому что это не степень двойки'''
def is_power_of_two(number):
    if not isinstance(number, int) or number <= 0:
        return "Wrong number"

    if (number & (number-1) == 0) and number != 0:
        return "yes"
    else:
        return "no"

print(is_power_of_two(256))
print(is_power_of_two(6))
print(is_power_of_two(3))
print(is_power_of_two(0))
print(is_power_of_two(8))
