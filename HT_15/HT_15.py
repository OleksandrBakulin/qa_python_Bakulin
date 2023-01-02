''''Написать итератор ReverseIterator который принимает список любых объектов и итерируется по ним в обратном порядке.
Важно: Нужно использовать аннотации.
Пример: it = ReverseIterator([1, 2, 3, 4, 5])
next(it)  # 5
next(it)  # 4
next(it)  # 3'''
class ReverseIterator:
    def __init__(self, data:[]):
        self.data = data
        self.index = len(data)

    def __next__(self):
        self.index -= 1
        if self.index < 0:
            raise StopIteration
        return print(f"next(it) # {self.data[self.index]}")


it = ReverseIterator(["damn", 2, 3.4, {"Key": "Word"}, 5])

next(it)
next(it)
next(it)
next(it)
next(it)
