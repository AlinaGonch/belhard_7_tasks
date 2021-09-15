"""
Создайте класс RandSequence с методами, формирующими вложенную последовательность.

Определить атрибуты:

- n - длина последовательности
- sequence - последовательность

Определить методы:

- инициализатор __init__, который принимает длину последовательности n и генерирует
    случайную последовательность длиной n в атрибут sequence
- метод generate, который принимает длину последовательности n (если n не передано,
    то сгенерировать длиной self.n) и генерирует последовательность в атрибут sequence.
    Для получения некоторого рандомного числа - воспользоваться функцией
    random.randint(-n, n)
- метод print_seq, который выводит последовательность на экран
"""
import random


class RandSequence:
    n: int
    sequence: list

    def __init__(self, n):
        self.n = n
        self.sequence = [random.randint(-self.n, self.n) for i in range(self.n)]

    def generate(self, new_n=None):
        if new_n is not None:
            self.sequence = [random.randint(-new_n, new_n) for i in range(new_n)]
        else:
            self.sequence = [random.randint(-self.n, self.n) for i in range(self.n)]

    def print_seq(self):
        print(f'{self.sequence}')


if __name__ == '__main__':
    seq = RandSequence(5)
    seq.generate()
    seq.print_seq()
