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
    def __init__(self, root):
        self.root = root
        self.root.title('Графический редактор')
        self.root.geometry("600x600")
        self.root.resizable(False, False)


# Делаем стартовые настройки.
        self.color = 'red'
        self.line_width = 10

        self.last_x, self.last_y = None, None

# Следующий шаг меню:
        self.menu_bar = Menu(self.root)
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label='Выход', command=self.root.quit)
        self.menu_bar.add_cascade(label='Файл', menu=self.file_menu)
        self.root.config(menu=self.menu_bar)

# Холст
        self.canvas = Canvas(self.root, bg='white')
        self.canvas.pack(fill=BOTH, expand=True)


# Панель инструментов
        self.toolbar = Frame(self.root, bg = 'light grey', height=40)
        self.toolbar.pack(fill=X, side=BOTTOM)

# Палитра цветов
        self.colors = ['red', 'green', 'blue', 'black']
        for color in self.colors:
            btn = Frame(self.toolbar, bg=color, width=40, height=30, cursor='hand2')
            btn.pack(side=LEFT, padx=2, pady=5)
            btn.bind('<Button-1>', lambda event, c=color: self.set_color(c))

# Поле ввода толщины и кнопка для подтверждения
        self.label_width = Label(self.toolbar, text='Толщина линии', font=('Arial', 13))
        self.label_width.pack(side=LEFT, padx=(20, 5))

        self.width_entry = Entry(self.toolbar, width=5)
        self.width_entry.insert(0, str(self.line_width))
        self.width_entry.pack(side=LEFT, padx=5)


        self.btn_set_width = Button(self.toolbar,
                                    text='Установить толщину', font=('Arial', 14),
                                    command=self.update_width)
        self.btn_set_width.pack(side=LEFT, padx=5)


# Привязка событий к кнопкам мыши (к холсту):
        self.canvas.bind('<Button-1>', self.start_draw)
        self.canvas.bind('<B1-Motion>', self.draw)


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

        self.last_x, self.last_y = event.x, event.y


    def draw(self, event):

        if self.last_x and self.last_y:
            self.canvas.create_line(
                self.last_x, self.last_y,
                event.x, event.y,
                fill=self.color, width=self.line_width,
                capstyle=ROUND, smooth=True
            )
        self.last_x, self.last_y = event.x, event.y




if __name__ == '__main__':
    root = Tk()
    app = DrawApp(root)
    root.mainloop()

