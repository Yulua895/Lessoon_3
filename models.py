class Card:
    balance: float = 1000000  # баланс на карте
    def __init__(self, num, owner):  # карта должна иметь номер и пользователя.
        self.num = num
        self.owner = owner
        self._count = 0  # Добавляем счетчик - это количество транзакций.

# Пропишем доступ к счетчику (count):
    @property
    def count(self):
        return self._count

    @count.setter  # происходит переопределение
    def count(self, value):
        self._count = value


# Пропишем статический метод, который позволит мне передать на баланс какое-то значение и увидеть баланс карты:
    @staticmethod
    def deposit(self, amount):  # deposit - будет увеличивать баланс карты
        self.balance += amount

    def credit(self):  # с помощью credit будем уменьшать баланс на карте
        if Card.balance > 0:
            self.count += 1
            # self.balance -= 1
            Card.balance -= 1
            return True
        else:
            print(f'На карте {self.num} недостаточно средств')
        # self.balance -= amount


    def __str__(self):  # прописываем для того, чтобы иметь представление что из себя представляет наша карта
        return (f'\nКарта: {self.num}\n'
                f'Выдана: {self.owner}\n'
                f'Количество операций: {self._count}')


# Необходимо описать класс транзакций (по сути дела потока) потому что
# каждый банкомат создает свой вход (поток) в систему. СМОТРИ НОВЫЙ ФАЙЛ, КОТОРЫЙ НАЗЫВАЕТСЯ threads (потоки).