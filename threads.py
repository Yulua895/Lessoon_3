from threading import Thread, Lock  # делаем синхронизацию потоков, через класс Lock

from models import Card



class Transaction (Thread):
    lock = Lock()  # определили его в class Transaction, как статический атрибут
    def __init__(self, amount, card: Card):  # amount - это сумма, которая будет снята с карты.
        super().__init__()
        self.amount = amount
        self._card = card


    @property
    def card(self):
        return self._card


    def run(self):  # метод, который пропишет нам начало транзакций
        print(f'Начало транзакций >= {self.card}')
        for k in range(self.amount):
            with Transaction.lock:
                if not self.card.credit():
                    break
        print(f'Конец транзакций >= {self.card}')