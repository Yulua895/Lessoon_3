class Stack:
    def __init__(self, data=[], limit=None):
        self.data = data
        self.limit = limit


    def push(self, obj):  # функция, которая будет добавлять
        if self.limit and len(self.data) < self.limit:
            self.data.append(obj)
        else:
            return f'Стек уже заполнен!'


    def pop(self):  # забор
        if self.data:
            return self.data.pop()
        else:
            return None

# Метод, который покажет нам длину:
    def __len__(self):
        return len(self.data)


    def empty(self):
        return len(self) == 0


# Увидеть стэк:
    def __str__(self):
        return self.data


# Создание экземпляра класса:
s1=Stack(limit=2)
s1.push(5)
s1.push(6)
print(s1.push(7))
print(s1.empty())
