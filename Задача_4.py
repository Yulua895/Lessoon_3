# Условие задачи:

# Доработайте проект калькулятора. Добавьте кнопку для умножения трех чисел.

# Решение:

from tkinter import Tk, Button, Label, Entry, messagebox

# from calc_dz import result

W, H = 360, 220

def calc_summ():
    try:
        num1 = float(value1.get())
        num2 = float(value2.get())
        num3 = float(value3.get())
        res = num1 + num2 + num3
        result.config(text=f'Сумма трех чисел: {num1} + {num2} + {num3} = {res}',
                        bg='#F54927')
    except ValueError:
        messagebox.showerror('Ошибка ввода', 'Прошу вводить корректные числа')


def calc_prod():
    try:
        num1 = float(value1.get())
        num2 = float(value2.get())
        num3 = float(value3.get())
        res = num1 * num2 * num3
        result.config(text=f'Произведение трех чисел: {num1} * {num2} * {num3} = {res}',
                      bg='orange')
    except ValueError:
        messagebox.showerror('Ошибка ввода', 'Прошу вводить корректные числа')


root = Tk()
root.title('Калькулятор')
root.geometry(f'{W}x{H}')
root.resizable(False, False)

Label(text='Введите три числа и нажмите на кнопку для вычисления суммы').pack()
value1 = Entry()
value1.pack(pady=(5, 0), padx=5)
value2 = Entry()
value2.pack(pady=(5, 0), padx=5)
value3 = Entry()
value3.pack(pady=(5, 0), padx=5)


Button(text='Сложить три числа', command=calc_summ).pack(pady=5)
Button(text='Умножить три числа', command=calc_prod).pack(pady=5)

result = Label(font=('Arial', 10, 'bold'))
result.pack(pady=(10, 0))

root.mainloop()

