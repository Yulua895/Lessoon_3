"""Множественное наследование, статические атрибуты"""



# Сделаем базовый класс для play:
class MixinPlay:
    @staticmethod
    def play(channal = 1):  # канал по умолчанию равен единице.
# Внесем в него какое-либо разнообразие:
        match channal:
            case 1: print('Звучит "Beatles" ')
            case 2: print('Звучит "АВВФ" ')
            case 3: print('Звучит "Leps" ')
            case 4: print('Звучит "Новостной канал" ')
            case 5: print('Звучит "Концерт Игоря Крутого" ')



class Car(MixinPlay): # подмешаем MixinPlay класс в класс Car
    name = 'Автомобиль'  # это статическое поле
    def ride(self):
        print(f'Как {Car.name} Едет по дороге')

    # def play(self):
    #     print('Звучит "Beatles"')
    # @staticmethod  # При помощи этого прописали, что это статик метод (т.е. повесив на него декоратор, который будет называться staticmethod)
    # def play():
    #     print('Звучит "Beatles"')


class Boat(MixinPlay): # подмешаем MixinPlay класс в класс Boat
    def swim(self):
        print('Ходит по воде')


    # def play(self):
    #     print('Звучит "АВВА"')
    # @staticmethod  # При помощи этого прописали, что это статик метод (т.е. повесив на него декаратор, который будет называться staticmethod)
    # def play():
    #     print('Звучит "АВВА"')


class Amphibian(Car, Boat):  # class Amphibian наследуется от 2-ух классов одновременно.
    # Здесь я могу вызвать и метод display и метод ride и метод swim.
    def display(self):
        print('Амфибия:')

# Создадим объект класса Car, Boat:
# car = Car() # у него есть единственный метод и этот метод ride. И мы его можем применить (строка 15)
# boat = Boat()  # у него есть единственный метод и этот метод swim. И мы его можем применить (строка 16)
# car.ride()  # Результат: Едет по дороге
# boat.swim()  # Результат: Ходит по воде
am = Amphibian()
am.display()
am.ride()
am.swim()

# Класс Amphibian является и объектом класса Car и
# одновременно является и объектом класса Boat.
# print(isinstance(am, Car))  # Результат: true
# print(isinstance(am, Boat))  # Результат: true
# print(isinstance(am, Amphibian))  # Результат: true
# Поэтому, если один и тот же метод будет написан в обоих классах то -
# это полиморфизм
# am.play()

# Статическое озночает, что она доступна для любого объекта, например, класса Car.

# Динамические поля или методы - это когда есть self и они принадлежат конкретному экземпляру класса. Например:
# def play(self):
    #     print('Звучит "АВВА"')

# принадлежат всем экземплярам сколько мы объектов класса не построили
# у всех будет одинаково отрабатывать метод def (self)
am.play(1)
am.play(3)
am.play(5)

# Ромбовидное наследование это класс MixinPlay, когда жесткой привязки к статическим методам уже нет.

# Нарисуем класическое ромбовидное наследование:
class A:
    def display(self):
        print('A')


class B (A):  # Класс В наследуется от класса А
    pass
    # def display(self):
    #     print('B')


class C (A):  # Класс С наследуется от класса A
    pass
    # def display(self):
    #     print('C')


class D (B, C):  # Класс D наследуется от класса B и C
    pass
    # def display(self):
    #     print('D')



# Как отработает метод display?
print(D.mro())
obj = D()  # Создаем объект класса D
obj.display()  # Результат: D. После того как мы закоментировали строчки кода 96 и 97
# мы полцчили Результат: В


# Создадим родительские классы для выполнения функции конструктора.

class Name:
    def __init__(self, name):
        self.name = name


class Age:
    def __init__(self, age):
        self.age = age

# Далее делаем наследника от этих классов:

class Human(Name, Age):
    def __init__(self, name, age):
        super().__init__(name)  # super() всегда показывает первый класс. Т.е. в данном случае Name.
# А Age будет выглядеть следующим образом:
        Age.__init__(self, age)

    # def __str__(self):
    #     return f'{self.name} is {self.age} years old'

    def __repr__(self):
        return f'{self.name} - {self.age} '

# Теперь я создам объект класса:
h = Human('Harry', 19)
h1 = Human('John', 23)
print(h)
# Создадим список объектов h и h1
humans = [h, h1]
print(humans)  # список не знает как вывести объект класса Human. Чтобы
# это получилось нам нужен метод repr (смотри выше)






