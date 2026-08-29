from tkinter import *
import math



def add(n1, d1, n2, d2):
    n = n1 * d2 + n2 * d1
    d = d1 * d2
    return n, d


def sub(n1, d1, n2, d2):
    n = n1 * d2 - n2 * d1
    d = d1 * d2
    return n, d


def mult(n1, d1, n2, d2):
    n = n1 * n2
    d = d1 * d2
    return n, d


def div(n1, d1, n2, d2):
    n = n1 * d2
    d = d1 * n2
    return n, d

# В результате этих действий с высокой степенью вероятности мы получаем неправильную дробь.
# Чтобы получить результат нам нужно найти наибольший общий делитель и сократить эту дробь.


def calk():
    try:
        n1 =int(num1.get())
        d1 =int(den1.get())
        n2 = int(num2.get())
        d2 = int(den2.get())
        operator = oper.get().strip()
        res = (0, 1)
        #res = None # это строчка означает, что у результата нет значения
# Проанализируем операторы:
        match operator:
            # Присвоим их какому-либо значению res (первичный результат)
            case '+': res = add(n1, d1, n2, d2)# Если будет +,
            # то вы вызовем функцию add и передадим в нее аргументы n1, d1, n2, d2.
            case '-': res = sub(n1, d1, n2, d2)
            case '*': res = mult(n1, d1, n2, d2)
            case '/': res = div(n1, d1, n2, d2)
# Получим наибольший общий делитель (в библиотеке math есть функция, которая называется gcd)
        nod = math.gcd(res[0], res[1])
        n = int(res[0] / nod)
        d = int(res[1] / nod)
        int_p = ''  # целая часть
        if n > d: # если числитель n больше знаменателя d, то я должна получить целую часть int_p
            int_p =n // d
            n = n % d # остаток от деления
        if n == 0:
            n = ''
            d = ''
        if n == d and int_p == '':
            n = ''
            d = ''
            int_p = 1
        int_part.config(text=int_p)
        num3.config(text=n)
        den3.config(text=d)



    except Exception:  # все ошибки
        pass # делать в ней ничего не будем



root = Tk()  # обязательный корневой элемент
WIDTH = root.winfo_screenmmwidth()  # Ширина экрана, как константа (написано с большой буквы).
HEIGHT = root.winfo_screenmmheight()  # Высота экрана, как константа (написано с большой буквы).
X = 400
Y = 250

# root.geometry("400x250+400+200")  # напишем блок смещения (+400+200), чтобы окошко располагалось по центру.
root.geometry(f"{X}x{Y}+{WIDTH  // 2 - X // 2}"
              f"{HEIGHT // 2 - Y // 2 - 20}")  # Мы это указываем, чтобы на любом экране компьютера это окошко располагалось посередине.
root.title('Калькулятор дробей')
frame = Frame(root) # Построим отдельный фрейд (выделю отдельную область в базовом окне)
frame.pack(pady=10) # Разместим frame в менеджере pack

# ВО frame МЫ ИСПОЛЬЗУЕМ ТОЛЬКО grid


# Поставим 1-ое окошечко (числитель и знаменатель)
num1 = Entry(frame, width=2) # числитель
num1.config(font=('Arial', 15), justify='center')
# num1.pack(pady=10)
num1.grid(row=0, column=0) # этот числитель будет находится в нулевой строке и в нулевой колонке

# Нарисуем линию, которая будет подчеркивать (разделять) числитель и знаменатель
line1 = Label(frame, text=chr(8212)*3)  # код длинного тире - chr(8212)
line1.grid(row=1, column=0)

den1 = Entry(frame, width=2) # знаменатель
den1.config(font=('Arial', 15), justify='center')
den1.grid(row=2, column=0) # этот знаменатель будет находится во второй строке и в нулевой колонке

# Поставим оператор:
oper = Entry(frame, font=('Arial', 15),  width=2)
oper.config(justify='center')
oper.grid(row=1, column=1, padx=5) # row=1, column=1 такие значения, чтобы он был посередине.

# Сделаем вторую дробь
num2 = Entry(frame, width=2) # числитель
num2.config(font=('Arial', 15), justify='center')
num2.grid(row=0, column=2) # этот числитель будет находится в нулевой строке и в нулевой колонке

# Нарисуем линию, которая будет подчеркивать (разделять) числитель и знаменатель
line2 = Label(frame, text=chr(8212)*3)  # код длинного тире - chr(8212)
line2.grid(row=1, column=2)

den2 = Entry(frame, width=2) # знаменатель
den2.config(font=('Arial', 15), justify='center')
den2.grid(row=2, column=2)

# Сделаем кнопку, которая при нажатии начала срабатывать механизм расчета.
btn = Button(frame, text='=', width=2, command=calk)
btn.config(font=('Arial', 15))
btn.grid(row=1, column=3, padx=5)

# Выделим окно под целую часть и под дробь
int_part = Label(frame,text='   ', bg='light gray')
int_part.config(font=('Arial', 20), width=2, justify='center')
int_part.grid(row=1, column=4)
# Создаем окно для дроби
num3 = Label(frame, width=2, bg='light gray') # числитель
num3.config(font=('Arial', 15), justify='center')
num3.grid(row=0, column=5) # этот числитель будет находится в нулевой строке и в нулевой колонке

# Нарисуем линию, которая будет подчеркивать (разделять) числитель и знаменатель
line3 = Label(frame, text=chr(8212)*3)  # код длинного тире - chr(8212)
line3.grid(row=1, column=5)

den3 = Label(frame, width=2, bg='light gray') # знаменатель
den3.config(font=('Arial', 15), justify='center')
den3.grid(row=2, column=5)

# frame - ЭТО ОБЛАСТЬ В ОБЛАСТИ. МЫ ЕЕ ВВОДИМ ДЛЯ ТОГО, ЧТОБЫ УДОБНО БЫЛО РАБОТАТЬ.

# Нужна функция для расчета дробей. Назовем ее command=calk




root.mainloop()