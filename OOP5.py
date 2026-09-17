""""Абстрактные классы"""
# Это классы, которые сами по себе используются только как базовые и
# это классы определяющие, какие методы обязательно должны быть у тех классов, которые мы у них наследуем.
# Для того, чтобы работать с абстрактными классами нужно взять и импортировать 2 класса,
# которые выглядят следующим образом:
from abc import ABC, abstractmethod  # ABC - обозначает абстрактный класс. abstractmethod - обозначает абстрактный метод.
import math
class Shape(ABC):  # класс Фигура
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calk_square(self):  # Рассчитывание площадей
        pass

    def display(self):
        return self.name  # здесь метод display вернет саму фигуру self.name.



class Circle(Shape):  # создали класс, который рассчитает площадь круга
    def __init__(self, radius):
        super().__init__('Круг')
        self.radius = radius

    def calk_square(self):  # здесь мы прописываем рассчеты
        return math.pi * self.radius ** 2
# пропишем метод, который позволит вывести результат на экран:
    def display(self):
        # print(self.name)
        super().display()
        print(f'Радиус: {self.radius} ед. \n'
              f'Площадь: {self.calk_square():.2f} кв.ед')  # :.2f - означает ограничение числа двумя цифрами после запятой.



class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__('Прямоугольник')
        self.width = width
        self.height = height

    def calk_square(self):
        return self.width * self.height

    def display(self):
        super().display()
        print(f'Ширина: {self.width} ед. \n'
              f'Высота: {self.height} ед.\n'
              f'Площадь: {self.calk_square()} ед. ')  # calk_square - это метод, который всегда прописывается в скобочках.


class Gadget(ABC):
    @abstractmethod
    def display(self):
        pass

# Пропишем метод, который обеспечивает разговор.
    @abstractmethod
    def talk(self):
        pass

    # Пропишем метод, который обеспечивает интернет.
    @abstractmethod
    def inet(self):
        pass

# class Smartphone(Gadget):
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print('Обеспечивает разговор')
#
#     def inet(self):
#         print('Обеспечивает передачу данных')
#
#     def display(self):
#         print('Обеспечивает отображение данных')


# class Telephone(Gadget):
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print('Обеспечивает разговор')
#
#
#
#     def inet(self):
#         pass
#
#
#     def display(self):
#         pass

# Я не могу создать объект без остальных классов.
# Если не будет хоть одного класса прописан в классе Telephone то он не будет работать.
    # Я обязан их туда вписать, даже если они будут пустыми. И это как минимум неудобно.
    # Поэтому существуют принципы разделения интерфейсов. Он заключается в множественном наследовании.
# Мы будем делать все иначе. Мы не будем создавать класс Smartphone, а будем создавать класс Talk.
# Т.е. непосредственно функционал

class Talk(ABC):
    @abstractmethod
    def talk(self):
        pass

class Inet(ABC):
    @abstractmethod
    def inet(self):
        pass

class Display(ABC):
    @abstractmethod
    def display(self):
        pass

class Smartphone(Talk, Inet, Display):
    def __init__(self, name):
        self.name = name

    def talk(self):
        print('Обеспечивает разговор')

    def inet(self):
        print('Обеспечивает передачу данных')

    def display(self):
        print('Обеспечивает отображение данных')


class Telephone(Talk):
    def talk(self):
        print('Обеспечивает разговор')



if __name__ == '__main__':
    pass
    # c = Circle(5)  #  5 - это значение радиуса
    # c.display()
    # rect = Rectangle(4, 5)
    # rect.display()


# ИТОГ: мы моздаем по функциям нужный нам набор классов и потом
# мы их просто напросто используем. Это называется принцип разделения интерфейсов
# и используется он как раз для абстрактных классов, а это удобно.
# Абстрактный класс обязывает метод соотвествующие прописывать.

