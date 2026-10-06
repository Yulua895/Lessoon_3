
import requests  # позволяет отправлять запросы к веб-сервисам, получать данные от API и взаимодействовать с веб-страницами.

from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk





def update_currency_label(event):  # функция, которая будет вызываться автоматически через байт
    code = combobox.get()
    name = currencies[code]
    currency_label.config(text=name)


def exchange():

    code = combobox.get()
    if code:

        try:
            result = requests.get('https://www.coingecko.com/en/api')
            result.raise_for_status()  # если вдруг чего, то она сразу отправит в Exception с кодом ошибки
            data = result.json()
            if code in data['rates']:
                exchange_rate = data['rates'][code]
                currency_name = currencies[code]
                mb.showinfo('Курс обмена',
                                f'Курс к доллару'
                                f' {exchange_rate:.1f} {currency_name} за 1 $')
    # В противном случае, если кода нет
            else:
                mb.showerror('Ошибка', f'Валюта {code} не найдена')

        except Exception as e:
            mb.showerror('Ошибка', f'error 400 {e}')  # error 400 - сайт нас совсем не понял





currencies = {
    'USD': 'Доллар США',
    'EUR': 'Евро',
    'CNY': 'Юань',
    'RUB': 'Российский рубль'
}

pop_curr = ['EUR', 'USD', 'RUB', 'CNY']  # как строится combobox?. Мы создаем список каких-то валют, которые мы там знаем

# Пропишем оконные приложения:
root = Tk()
root.title('Курс валют по отношению к доллару США')
root.geometry('500x500')
# Пропишем окошечко для ввода валюты:
Label(text='Введите код валюты').pack(pady=10, padx=10)
combobox = ttk.Combobox(values=pop_curr)
combobox.pack()
currency_label = ttk.Label()
currency_label.pack(pady=10, padx=10)
# Ниже прописывает то, что позволит нам ввести значение:
button = Button(text='Получить курс', command=exchange)  # введем клавишу, которая будет обеспечивать нам получить курс
button.pack(pady=10, padx=10)
combobox.bind('<<ComboboxSelected>>', update_currency_label)  # выбор


root.mainloop()