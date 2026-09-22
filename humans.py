# !!!! Дописать условие задачи из github Игоря Леонидовича !!!!

class Human:
    def __init__(self, name, *essence, magic=0):
        self.name = name
        self.magic = magic
        self.essence = list(essence)



    def change_name(self, name):
        self.name += ' ' + name


    def __add__(self, line):  # берем специальную переменную
        self.essence.append(line)
        self.magic += len(line)  // 4
        return self

    def __call__(self, num):
        return self.essence[:num]

    def __sub__(self, other):
        name = self.name[:3] + other.name[-3:].capitalize()  # [:3] - вырезаем буквы от начала до трех.
        # capitalize() - метод сделает первую букву в слове большую.
        essence = list(set(self.essence) - set(other.essence))
        essence.sort()  # сортировка по алфавиту
        return Human(name, *essence, magic=0)

    def __eq__(self, other):  # метод, который используется для сравнения
        if self.magic == other.magic:
            if len(self.essence) == len(other.essence):
                if self.name == other.name:
                    return True
        return False

    def __gt__(self, other): # метод, который используется для сравнения больше
        if self.magic > other.magic:
            return True
        elif self.magic == other.magic and len(self.essence) > len(other.essence):
            return True
        elif self.name > other.name and len(self.essence) == len(other.essence):
            return True
        return False


    def __lt__(self, other): # метод, который используется для сравнения меньше
        if self.magic < other.magic:
            return True
        elif self.magic == other.magic and len(self.essence) < len(other.essence):
            return True
        elif self.name < other.name and len(self.essence) == len(other.essence):
            return True
        return False


    def  __le__(self, other): # метод, который используется для сравнения меньше или равно
        if self.magic <= other.magic:
            return True
        else:
            return False


    def __ne__(self, other):  # метод, который используется для сравнения не равно
        if (self.magic != other.magic or len(self.essence) != len(other.essence)
        or self.name != other.name):
            return True
        return False





    def __str__(self):
        return f'Человек по имени {self.name} ({", ".join(self.essence)}, {self.magic})'



# hm = Human('Illmarrannen', 'Forgiving', 'Forgiven', magic=2)
# hm.change_name('Rual')
# id_hm = id(hm)
# hm += 'Skyman'
# print(hm, hm(2), sep='\n')
# print(id_hm == id(hm))
# print(hm)


hm = Human('Marran', 'Hanger', 'Stick', 'Wizzard', magic=10)
hm1 = Human('Lart', 'Wizzard')
print(hm, hm1, sep='\n')
print(hm > hm1, hm <= hm1, hm == hm1)
hm2 = hm - hm1
print(hm2)
print(hm2 > hm1, hm2 <= hm, hm2 != hm)
