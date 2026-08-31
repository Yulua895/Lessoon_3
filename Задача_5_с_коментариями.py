# Условие задачи:

# Добавьте в проект графического редактора возможность изменения
# толщины пера с помощью поля ввода (Entry) и кнопки. Это позволит
# пользователям вводить желаемую толщину пера. Добавьте поле ввода
# для задания толщины линии.

# 1. Добавьте кнопку установки толщины пера.
# 2. Создайте функцию для обновления толщины пера с обработкой исключения
# ValueError, которое может возникнуть, если в поле ввода толщины будет введено
# не целое число.
# 3. Обновите функцию draw, чтобы она использовала значение толщины,
# введенное пользователем.


# Решение:
from tkinter import Canvas, Frame, Menu, Label, Button, Tk
from tkinter import Entry, BOTH, X, BOTTOM, LEFT, ROUND
from typing import NamedTuple


class DrawApp:
    def __init__(self, root): # Далее напишем, что в этот root входит
        self.root = root  # Делаем корневой элемент приложения уже элементом нашего класса
        self.root.title('Графический редактор')
        self.root.geometry("600x600")
        self.root.resizable(False, False)

# Делаем стартовые настройки.
# У нас по условию задачи линия должна рисоваться каким-то цветом и с какой-то толщиной.
        self.color = 'red'
        self.line_width = 10
# Всегда нужны координаты точки. То есть рисовать на экране мы будем при помощи мыши.
# И от одной точки до другой мы будем все это соединять линиями.
# И каждый раз нам нужно запоминать координаты предыдущей точки. Ну или последней точки при которой мы отпустили кнопку мыши.
# Поэтому напишем:
        self.last_x, self.last_y = None, None

# Следующий шаг меню:
        self.menu_bar = Menu(self.root)
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label='Выход', command=self.root.quit)
        self.menu_bar.add_cascade(label='Файл', menu=self.file_menu)
        self.root.config(menu=self.menu_bar)

# Холст
        self.canvas = Canvas(self.root, bg='white')
        self.canvas.pack(fill=BOTH, expand=True) # BOTH - заполнить холст по х и по у. expand=True (развернуть оригинал)


# Панель инструментов отдельным фреймом
        self.toolbar = Frame(self.root, bg = 'light grey', height=40) # в скобках указываем, куда мы прикрепляем этот Frame.
        self.toolbar.pack(fill=X, side=BOTTOM) # fill=X - линейка снизу

# Палитра цветов
        self.colors = ['red', 'green', 'blue', 'black']
        for color in self.colors:
            btn = Frame(self.toolbar, bg=color, width=40, height=30, cursor='hand2')
            btn.pack(side=LEFT, padx=2, pady=5)
            btn.bind('<Button-1>', lambda event, c=color: self.set_color(c))  # передаем событие (event) и цвет с

# Поле ввода толщины и кнопка для подтверждения
        self.label_width = Label(self.toolbar, text='Толщина линии', font=('Arial', 13))
        self.label_width.pack(side=LEFT, padx=(20, 5))

        self.width_entry = Entry(self.toolbar, width=5) # из Entry все, что приходит и все, что в Entry отправляется обязательно должно быть в виде строки
        self.width_entry.insert(0, str(self.line_width))
        self.width_entry.pack(side=LEFT, padx=5)


        self.btn_set_width = Button(self.toolbar,
                                    text='Установить толщину', font=('Arial', 14),
                                    command=self.update_width)
        self.btn_set_width.pack(side=LEFT, padx=5)


# Привязка событий к кнопкам мыши (к холсту):
        self.canvas.bind('<Button-1>', self.start_draw) # '<Button-1>' - левая кнопка мыши. '<Button-2>' - средняя кнопка мыши. '<Button-3>' - правая кнопка мыши.
        self.canvas.bind('<B1-Motion>', self.draw) # '<B1-Motion>' - перемещение мыщи с зажатой левой клавишой


    def set_color(self, new_color):
        self.color = new_color


    def update_width(self):
        try:
            temp = int(self.width_entry.get())
            if 0 < temp < 30:
                self.line_width = temp
            else:
                self.line_width = 10
        except ValueError:
            pass


    def start_draw(self, event):
# Фиксация координат клика мыши при начале рисования
        self.last_x, self.last_y = event.x, event.y


    def draw(self, event):
# Линия от точки к точке при движении мыши
        if self.last_x and self.last_y:
            self.canvas.create_line(
                self.last_x, self.last_y,
                event.x, event.y,
                fill=self.color, width=self.line_width,
                capstyle=ROUND, smooth=True  # Концы линии будут закругленными и сглаженной
            )
        self.last_x, self.last_y = event.x, event.y



# Сделаем вызов нашего приложения:
if __name__ == '__main__':
    root = Tk()
    app = DrawApp(root) # создаем наше приложение. app (application) - приложение
    root.mainloop()

