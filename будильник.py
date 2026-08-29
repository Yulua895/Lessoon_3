from _pyrepl import commands
from threading import current_thread
from tkinter import *  # Импортируем  все из библиотеки tkinter
from time import strftime # Библиотека времени
from calc_dz import result
from tkinter import messagebox  # библиотека сообщений
import pygame as pg



def tick():
    global time_run
    current_time = strftime('%H:%M:%S')  # в скобках указываем нужный нам формат времени
    current_time1 = strftime('%H:%M')
    current_time2 = strftime('%H')
    text.config(text=current_time)
    if (time_run == current_time or time_run == current_time1
            or time_run == current_time2):
        time_run = ''
        pg.mixer.music.play()
    text.after(1000, tick)


def on():  # Данная функция должна получить время из поля ввода
    global time_run
    time_run =  entry.get().strip()  # функция get() заберет все, что есть. Это ничто иное, как строка.
    messagebox.showinfo('Время установки будильника',
                        f'Будильник установлен на {time_run}')

def off():
    global time_run  # Для чего мы пишем глобал? Если мы хотим какую-либо переменную, которая используется разными функциями, но она одна и таже.
    # Мы ее прежде всего должны определить, как переменную нашего модуля. И в каждой функции, которую мы будем применять к нейкакие-либо изменения определить ее, как глобальную.
    # Потому что в противном случае это будут разные переменные.
    time_run = ''
    pg.mixer.music.stop()
    messagebox.showwarning('Предупреждение',
                        f'Будильник отключен! {time_run}')

pg.mixer.init()  # здесь мы активировали данную библиотеку
pg.mixer.music.load('music.mp3')# загружаем тот модуль, который у нас будет работать
time_run = ''
root = Tk()# обязательный корневой элемент
root.config(background='black')
WIDTH = root.winfo_screenmmwidth()  # Ширина экрана, как константа (написано с большой буквы).
HEIGHT = root.winfo_screenmmheight()  # Высота экрана, как константа (написано с большой буквы).
X = 400
Y = 250

# root.geometry("400x250+400+200")  # напишем блок смещения (+400+200), чтобы окошко располагалось по центру.
root.geometry(f"{X}x{Y}+{WIDTH  // 2 - X // 2}"
              f"{HEIGHT // 2 - Y // 2 - 20}")  # Мы это указываем, чтобы на любом экране компьютера это окошко располагалось посередине.
root.title('Будильник')

# Организуем виджеты/окна (какие-то элементы, которые имеют строго определенный функционал):
# виджет Label() просто сделает надпись, виджет Entry() поможет ввести значения.
# А сделать кнопку виджет Button().

text = Label(root, text='00:00:00')
#  Размещение информации в окнах виджетах осуществляется специальными менеджерами разметки.
#  Их в tkinter 3: pack(), green(), play().
text.pack()
# text.pack(side= TOP)  # по умолчанию используется ТОР.
#
# text.pack(side= LEFT)  # размещение текста слева.
# text.pack(side= RIGHT)  # размещение текста справо.
# text.pack(side= BOTTOM)  # размещение текста внизу.
text.config(font=('Arial', 50), bg='black', fg='lime')  # Сделать больше шрифт. bg (бег граунд) - заливка. fg - изменение цвета самаго текста.
text.pack()
entry = Entry(root, font=('Arial', 20), width=10, justify=CENTER)  # Здесь ширину считаем не по количеству пикселей, а по количеству символов.
entry.pack()

tick()

# Сделаем разрыв между двумя этими окошками сверху и снизу.
# Или по другому отступы, которые называются padding.
entry.pack(pady=10)





# Можем организовать кнопку при помощи метода Button (btn).
btn = Button(text='Включить', width=10, font=('Arial', 10), command=on)
btn.pack(pady=5)
btn1 = Button(text='Выключить', width=10, font=('Arial', 10), command=off)
btn1.pack()


# Для того, чтобы отработать результат нам нужно каким-то образом привезать поле ввода
# к какой-то функции, которая выдаст нам этот результат. Напишем эту функцию в самом начале

# Центр координат расположен в левом верхнем углу.
# Ось у увеличивается сверху вниз, о ось х, как обычно, слево направо.
root.mainloop()  # обязательный замыкающий элемент
