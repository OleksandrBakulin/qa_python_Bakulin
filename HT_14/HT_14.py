'''Создайте супер класс Shape и его наследников Triangle, Rectangle.
Класс Shape содержит абстрактный метод draw
Класс Triangle в инициализаторе принимает параметр width: int - ширина треугольника и реализует метод draw
(Выводит в консоль треугольник с шириной width)
Класс Rectangle в инициализаторе принимает параметр width: int и height: int - ширина, высота прямоугольника
и реализует метод draw (Выводит в консоль прямоугольник с шириной width и высотой height)
Создайте список с этими фигурами и в цикле вызовите метод draw у этих обьектов

P.S. Треугольник может быть любой (Равносторонний, Равнобедренный, Разносторонним) главное чтобы состоял и был заполнен символом '*'.
Прямоугольник тоже должен состоять и быть заполнен символом '*'.
Важно: Используйте аннотации!'''

class Shape:
    def draw(self):
        raise NotImplementedError

class Triangle(Shape):
    def __init__(self, width: int):
        self.width = width
    def draw(self):
        if self.width > 0:
            for i in range(self.width + 1):
                print(i * "*")
                i -= 1
        else:
            print("the number should be more than 0")
class Rectange(Shape):
    def __init__(self,width : int, height :int ):
        self.width = width
        self.height = height

    def draw(self):
        if self.width > 0 and self.height > 0:
            for i in range(self.height):
                print(self.width * "*")
        else:
            print("the number should be more than 0")

a = Triangle(5)
a.draw()
print(" ")
b = Rectange(4,5)
b.draw()