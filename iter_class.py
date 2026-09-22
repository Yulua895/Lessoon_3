# Итератором является объект, который имеет у себя
# 2 метода:
class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def __iter__(self):  # метод __iter__ возврощает нам объект
        self.cnt = 0
        return self

    def __next__(self):
        obj = (self.name, self.model, self.year)
        if self.cnt < len(obj):
            res = obj[self.cnt]
            self.cnt += 1
            return res
        raise StopIteration


    def __str__(self):
        return f'{self.name} {self.model} {self.year}'




boat =['Name', 'Model', 'Year']
boat1 =['Name', 'Model', 'Year']
car =Car('Mercedes', 'S-222', 2015)
lst = [boat, boat, car]
for i in lst:
    # print(i)
    for j in i:
        print(j)