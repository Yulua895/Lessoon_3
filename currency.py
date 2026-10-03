
import requests
# import json
# import pprint
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def update_currency_label(event):  # функция, которая будет вызываться автоматически через байт
    #code = combobox.get()
    code = target_combobox.get()
    name = currencies[code]
    currency_label.config(text=name)



def exchange():
    # code = entry.get().strip().upper()
    #combobox.get()
    target_code = target_combobox.get()
    base_code = base_combobox.get()
    #if code:
    if target_code and base_code:
        try:
            result = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
            result.raise_for_status()  # если вдруг чего, то она сразу отправит в Exception с кодом ошибки
            # data = json.loads(result.text)
            data = result.json()
            # if code in data['reads']:
            if target_code in data['rates']:
                # exchange_rate = data['retes'][code]
                exchange_rate = data['rates'][target_code]
                # currencies_name = currencies[code]
                base = currencies[base_code]
                target = currencies[target_code]

                mb.showinfo('Курс обмена',
                            f'Курс '
                            f' {exchange_rate:.1f} {target} за 1 {base}')
# В противном случае, если кода нет
            else:
                mb.showerror('Ошибка', f'Валюта {target_code} не найдена')

        except Exception as e:
            mb.showerror('Ошибка', f'error 400 {e}')

# result = requests.get('https://open.er-api.com/v6/latest/USD')
# data = json.loads(result.text)  # result.text - должен нам вернуть джейсон файл. Будет возвращен в строковом типе данных
# print(data)
# print(type(data))  # Джейсон файл был представлен строкой текста
# Рассмотрим более детально:
# for item in data.items():
#     print(item)

# Можем тоже самое вывести при помощи ПППРИНТ
# p = pprint.PrettyPrinter(indent=4)
# p.pprint(data)
currencies = {
    'USD': 'Доллар США',
    'EUR': 'Евро',
    'CNY': 'Юань',
    'RUB': 'Российский рубль'
}

pop_curr = ['EUR', 'USD', 'RUB', 'CNY']  # как строится combobox?. Мы создаем список каких-то валют, которые мы там знаем


# Пропишем оконные приложения:
root = Tk()
# root.title('Курс валют по отношению к доллару США')
root.title('Курсы обмена валют ')
root.geometry('300x200')
# Пропишем окошечко для ввода валюты:
# Label(text='Введите код валюты').pack(pady=10, padx=10)
Label(text='Базовая валюта').pack(pady=10, padx=10)

# combobox = ttk.Combobox(values=pop_carr)
# combobox.pack()
base_combobox = ttk.Combobox(values=list(currencies.keys()))  # это базовая валюта
base_combobox.pack()  # это базовая валюта


Label(text='Вторая базовая валюта').pack(pady=10, padx=10)

# combobox = ttk.Combobox(values=pop_carr)
# combobox.pack()
base_combobox = ttk.Combobox(values=list(currencies.keys()))  # это базовая валюта
base_combobox.pack()  # это базовая валюта



Label(text='Целевая валюта').pack(pady=10, padx=10)
target_combobox = ttk.Combobox(values=list(currencies))  # это целевая валюта
target_combobox.pack()  # это целевая валюта

currency_label = ttk.Label()
currency_label.pack(pady=10, padx=10)
# Ниже прописывает то, что позволит нам ввести значение:
# entry = Entry(width=10)
# entry.pack()
button = Button(text='Получить курс', command=exchange)  # введем клавишу, которая будет обеспечивать нам получить курс
button.pack()
# combobox.bind('<<ComboboxSelected>>', update_currency_label)
target_combobox.bind('<<ComboboxSelected>>', update_currency_label)


root.mainloop()