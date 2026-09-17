from typing import Union, Optional, List, Dict  # Optional - покажет, что объект может относится
# к какому-либо классу либо None. Union (объединение) показывает, что объект может состоять либо из такого
# либо из такого класса.

# Агрегирование - это когда объекты одного класса включают в себя объекты другого класса.

# Композиция или более распространеное ее наименование Агрегирование или Агрегация. Это,
# когда экземпляру класса допустим Person являются объектами класса Persons
# Расмотрим ее на примере:
class Person:
    def __init__(self, name, age):
        self.__name: str = name
        self.__age:int = age


# Для того, чтобы иметь возможность работать с этими полями в другом классе (неважно это наследник или доступ со стороны),
# мне понадобится декаратор @property
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


    def __str__(self):
        return f'{self.__name} - {self.__age}'


class Flat:
    """Класс описывающий квартиру"""
    def __init__(self, number):
        self.__number: int = number



# Композиция - это когда экземпляры одного класса включают в себя объекты другого класса.
# Т.е. есть класс Flat (какая-то квартира) и в этой квартире должны жить какие-либо люди. Так вот какие это люди будут - это
# будут объекты класса Person.
        self.__persons: List[Person] = []
# Если мы хотим что-либо сделать то нам понадобится  @property:
    @property
    def number(self):
        return self.__number

    @property
    def persons(self):
        return self.__persons

    def add_person(self, *persons: Person) -> None: # данный объект ничего не возврощает поэтому мы пишем None
        for person in persons:
            if not isinstance(person, Person):
                raise TypeError('Объект не является экземпляром класса "Persone"')
            self.__persons.append(person)

        # self.__persons.append(person)
        # self.__persons.extend(persons)  # метод extend к существующему списку длбавит другой список person


# Пропишем функцию, которая позволит нам выводить жителей квартиры:
    def display(self):
        max_name = max(self.__persons, key=lambda x: len(x.name))  # __persons - это
        # список объектоа класса Person. У каждого объекта класса Person есть name.
        # print(max_name)
        mx = len(max_name.name)
# Как сделать сквозную номерацию?
        print(self)
        for i, person in enumerate(self.__persons, 1):
            # print(f'\t\t\t{i}.{person.name:26} - {person.age}')
            print(f'\t\t\t{i}.{person.name:{mx}} - {person.age}')

    def __str__(self):
        return (f'\t\tКвартира: №{self.__number} ')

class Floor:
    def __init__(self, numb):
        self.__numb: int = numb
        self.__flats: List[Flat] = []

    @property
    def flats(self):
        return self.__flats

    @property
    def number(self):
        return self.__numb


    def add_flats(self, *flats: Flat) -> None:
        for flat in flats:
            if not isinstance(flat, Flat):
                raise TypeError('Объект должен быть экземпляром класса "Flat"')
            if flat.number > 999:
                raise ValueError('Номер не может быть больше 3-х знаков')
            self.__flats.append(flat)


    def display(self):
        # names = []
        # for flat in self.__flats:  # перебираем квартиры
        #     for person in flat.persons:
        #         names.append(person.name)


# Запишем со строчки 108 по 111 тоже самое, но сокращенно:
        # names = [person.name for flat in self.__flats for person in flat.persons]
        name_max = max((person.name for flat in self.__flats
                        for person in flat.persons), key=lambda x: len(x))
        mx = len(name_max)
        # print(names)
        # print(mx)
        print(self)
        count = 1
        for flat in self.__flats:
            print(flat)
            for person in flat.persons:
                print(f'\t\t\t{count:3}. {person.name:{mx}} - {person.age}')
                count += 1

    def __str__(self):
        return f'\tЭтаж №{self.__numb}: Количество квартир: - {len(self.__flats)}.'


class Dom:
    """Класс описывающий дом"""
    def __init__(self, num):
        self.__num: int = num
        self.__floors: List[Floor] = []

    @property
    def flats(self):
        return self.__flats

    @property
    def num(self):
        return self.__num

    def add_floors(self, *floors: Floor) -> None:
        for floor in floors:
            if not isinstance(floor, Floor):
                raise TypeError('Объект должен быть экземпляром класса "Floor"')
            if not isinstance(floor.number, int):
                raise TypeError('Номер этажа должен быть числом')
            self.__floors.append(floor)

    def display(self):
        name_max = max((person.name for floor in self.__floors
                        for flat in floor.flats
                        for person in flat.persons), key=lambda x: len(x))
        mx = len(name_max)
        print(self)
        count = 1
        for floor in self.__floors:
            print()
            print(floor)
            for flat in floor.flats:
                print(flat)
                for person in flat.persons:
                    print(f'\t\t\t{count:3}. {person.name:{mx}} - {person.age}')
                    count += 1





    def __str__(self):
        return f'Дом №{self.__num}'




# Далее стоит задача расселить людей. Для этого создаем реального человека:
# Создадим объекты класса Person:
p1 = Person('John Lenon', 33)
p2 = Person('Pol Mackartney', 43)
p3 = Person('Klava Koka', 30)
p4 = Person('Said Abdurahman ibn Hattab', 80)
p5 = Person('Ny', 12)
p6 = Person('John Lenon', 33)
p7 = Person('Pol Mackartney', 43)
p8 = Person('Klava Koka', 30)
p9 = Person('Said Abdurahman ibn Hattab', 80)
p10 = Person('Ny', 12)
# Создадим объекты класса Flat:
kv45 = Flat(45)
kv46 = Flat(46)
kv47 = Flat(47)
kv48 = Flat(48)
kv45.add_person(p1, p2)
kv46.add_person(p3, p4, p5)
kv47.add_person(p1, p2, p5)
kv48.add_person(p3, p4)
# kv45.display()
# kv46.display()
# print(Flat.__doc__) # смотри строка №39
f4 = Floor(4)  # этаж
f4.add_flats(kv45, kv46, kv47, kv48)
# f4.display()
# print(len('Said Abdurahman ibn Hattab'))

dom = Dom(25)
f5 = Floor(5)
#4.add_flats(kv45, kv46, kv47, kv48)
p11 = Person('John Lenon', 33)
p12 = Person('Pol Mackartney', 43)
p13 = Person('Klava Koka', 30)
p14 = Person('Said Abdurahman ibn Hattab', 80)
p15 = Person('Ny', 12)
p16 = Person('John Lenon', 33)
p17 = Person('Pol Mackartney', 43)
p18 = Person('Klava Koka', 30)
p19 = Person('Said Abdurahman ibn Hattab', 80)
p20 = Person('Ny', 12)

kv55 = Flat(55)
kv56 = Flat(56)
kv57 = Flat(57)
kv58 = Flat(58)
kv55.add_person(p11, p12)
kv56.add_person(p13, p14, p15)
kv57.add_person(p16, p17, p18)
kv58.add_person(p19, p20)
f5.add_flats(kv55, kv56, kv57, kv58)
dom.add_floors(f4, f5)
dom.display()  # выводим дом на экран.
# Как заселить людей в квартиры? В любом случае в классе Flat должен быть метод,
# который позволит нам кого-то куда-то заселить.


