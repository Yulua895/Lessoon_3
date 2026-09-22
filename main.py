# Здесь мы создаем основной файл к models и threads

from models import Card

from threads import Transaction

print(f'Начальный баланс - {Card.balance}')

# Далее выдадим карту сотрудникам:
card1 = Card(1234, 'Коля Колин')
card2 = Card(5678, 'Иван Иванов')

# Выполним транзакции, но перед этим определим потоки:
tran1 = Transaction(550000, card1)
tran2 = Transaction(550000, card2)

tran1.start()
tran2.start()
tran1.join()
tran2.join()


# Опишем ситуацию какая она будет:
print(f'Конечный баланс - {Card.balance}')
print(f'Число операций: {tran1.card.count + tran2.card.count}')
# Здесь у каждого потока есть карта
print(f'Дисбаланс: {1000000 - (tran1.card.count + tran2.card.count)} ')