'''
Необходимо создать класс Human с атрибутами:
name
surname
age
phone
address
Атрибуты должны заполняться в методе __init__
Так-же нужно написать методы:
get_info(self) - который возвращает словарь в котором находится информация о человеке
call(self, phone_number) - который будет выводить "{self.phone} вызывает абонента {phone_number}"
Нужно создать 3 обьекта класса Human и вызвать у них метод get_info
'''
class Human:
    def __init__(self, name: str, surname: str, age: int, phone: str, adress: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.adress = adress

    def get_info(self):
        dict = {"Name": self.name,"Surname": self.surname, "Age": self.age,"Phone": self.phone,"Adress": self.adress}
        return print(dict)
    def call(self, phone_number: str):
        print(f'{self.phone} calls abonent {phone_number}')

alex = Human("Alex","TheCodemaster",29,"+380971299","23Augusta")
ivan = Human("Ivan","Smith",19,"+3809014141","Heroiv Truda")
andrew = Human("Andrew","Levit",43 ,"+38097346235","Peremoha")
#
alex.get_info()
ivan.get_info()
andrew.get_info()

alex.call("+309993131")
ivan.call("+3809491314")