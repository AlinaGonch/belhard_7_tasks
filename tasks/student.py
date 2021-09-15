"""
Создать класс Student.

Определить атрибуты:

- surname - фамилия
- name - имя
- group - номер группы
- average_score - средний балл

Определить методы:

- инициализатор __init__
- Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
  студентов по среднему баллу

Создать список из 5 объектов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 5
"""


class Student:
    surname: str
    name: str
    group: int
    average_score: float

    def __init__(self, surname, name, group, average_score):
        self.surname = surname
        self.name = name
        self.group = group
        self.average_score = average_score

    def __eq__(self, other):
        return self.average_score == other

    def __ne__(self, other):
        return self.average_score != other

    def __lt__(self, other):
        return self.average_score < other

    def __gt__(self, other):
        return self.average_score > other

    def __le__(self, other):
        return self.average_score <= other

    def __ge__(self, other):
        return self.average_score >= other

    def get_info(self):
        return self.surname, self.name, self.group, self.average_score


student_list = [
    Student("Odin", "Odin", 10, 1.1),
    Student("Dva", "Dva", 17, 3.2),
    Student("TREE", "TREE", 13, 0.5),
    Student("Chet", "Chet", 9, 8.4),
    Student("Pallt", "Pallt", 10, -7.8)
]


if __name__ == '__main__':
    student_list.sort()
    for item in student_list:
        print(item.get_info())
    print('\n__REVERSED__')

    student_list.sort(reverse=True)
    for item in student_list:
        print(item.get_info())

    print('\n__More_than_5__')
    for item in student_list:
        if item > 5:
            print(item.get_info())
