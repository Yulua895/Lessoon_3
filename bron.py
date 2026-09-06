from tkinter import *


def color_(i):
    if i <= 3:
        color = 'red'
    elif 4 <= i <= 6:
        color = 'blue'
    else:
        color = 'yellow'
    return color



def handler(num):
    btns[num - 1].config(bg='light gray')

def unbuzy(num, row):
    color = color_(row)
    btns[num - 1].config(bg=color)



root = Tk()
root.title('Бронирование')
root.geometry('800x400+100+100')
frame1 = Frame(root)
frame2 = Frame(root)
frame1.pack(pady=10)
frame2.pack()

# Занимаемся экраном:
screen = Label(frame1, text='ЭКРАН')
screen.pack()
# Далее нарисуем этот экран и для этого нам потребуется холст
canvas = Canvas(frame1, width=400, height=60)
canvas.pack()

# нарисуем линии
canvas.create_line(50, 10, 350, 10, width=8, fill='light blue')  # верхнюю точку х и у начало линии (50 и 10). Конечную точку линии (350 и 10)
# Одна линия:
canvas.create_line(60, 40, 140, 40, width=4, fill='red')
# И в ней текст. Начальная позиция, где будет писаться:
canvas.create_text(100,30, text=1000)  # Как получили эту линию посередине (значение 100)? = (60 + 140)/2
canvas.create_line(160, 40, 240, 40, width=4, fill='blue')
canvas.create_text(200,30, text=1100)
canvas.create_line(260, 40, 340, 40, width=4, fill='yellow')
canvas.create_text(300,30, text=2000)

# Нарисуем места (где каждое место - это btn1):
# btn1 = Button(frame2)
# btn1.config(text=1, font='Arial 12', justify='center',
#             width=2, bg='red')
# btn1.grid(row=0, column=0)
#
# btn2 = Button(frame2)
# btn2.config(text=2, font='Arial 12', justify='center',
#             width=2, bg='red')
# btn2.grid(row=0, column=1)

# Сделаем несколько мест в ряду с помощью цикла for
rows = 10 # у нас есть 10 рядов
columns = 18 # и 18 мест в одном ряду
# Делаем список для кнопок:
btns = []
for i in range(rows):
    row = Label(frame2, text=f'Ряд № {i + 1}')
    row.grid(row=i, column=0)  # - прописали ряды
# Разрисуем колонки:
# Вложенность циклов (базовый цикл определяет нам строки, а вложенный цикл определяет колонки)
    for j in range(columns):
        num = i * columns + j + 1  # используется формула, которую необходимо запомнить.
        # if i <= 3:
        #     color = 'red'
        # elif 4 <= i <= 6:
        #     color = 'blue'
        # else:
        #     color = 'yellow'
        color = color_(i)
        btn = Button(frame2)
        btn.config(text=f'{j + 1}', font='Arial 12', justify='center',
                    width=2, bg=color, command=lambda x=num: handler(x))
        btn.grid(row=i, column=j + 1)

        btn.bind('<Button-3>', lambda event,  nm=num, r=i: unbuzy(nm, r))

        btns.append(btn)

# Далее при нажатии кнопки, если билет куплен мы должны занять это место. Для этого мы должны сделать функцию handler
# Сдать билет при помощи метода bind








root.mainloop()