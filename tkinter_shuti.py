import shutil
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
import os
from datetime import datetime

# shutil.copytree(r"C:\Users\yulya\OneDrive\Рабочий стол\Proba_shutil",
#                 r"C:\Users\yulya\OneDrive\Рабочий стол\Proba_shut_copy")
# copytrее - это
# метод, который позволит мне какой-то мой директорий. Для того, чтобы обратные слэши (например,
# \U он вопримет, как служебный символ) и в итогк сам машрут компьютер воспримет, как команду, чтонам не нужно. Чтобы
# это исправить необходимо экранировать слеши (т.е. делать их двойными) либо в начале поставить буковку r.

# shutil.move(r"C:\Users\yulya\OneDrive\Рабочий стол\Proba_shutil\shutil_1move",
#             r"C:\Users\yulya\OneDrive\Рабочий стол\Proba_shut_copy")  # беру папку и говорю куда мне ее перенести.
# Через запятую указываем, куда мы хотим ее перенести. ОТВЕЧАЕТ ЗА ПЕРЕМЕЩЕНИЕ.



root = Tk()
root.withdraw()  # выходим в диалоговый режим благодаря библиотеке withdraw()


dir_ = fd.askdirectory(title='Выбираем папку')  # метод askdirectory не принимает позиционные аргументы
# Выбрали папку и после этого мы должны проверить,
# если директория у нас была выбрана то мы после этого можем с ней что-то делать. А именно
# можем ее просмотреть
if dir_:
    for file in os.listdir(dir_):  # далее осуществляем отбор интересующих нас файлов
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):  # когда функция endswith работает,
            file_path = os.path.join(dir_,file)   # Есть библиотека операционной системы os и
# используя ее path мы работаем с машрутами. Так мы формируем путь (машрут).
            last_time = os.path.getmtime(file_path)  # получим по машруту os.path время, когда был создан этот файл.
            dt = datetime.fromtimestamp(last_time)
            dt = dt.strftime('%d-%m-%Y %X')

# то она может перибирать из вариаетов, которые мы прописали кортежом.
#             print(file)
            print(f'{file} изменен {dt}')

# Создадим перемещение нужных нам папок


root.mainloop()

# С помощью инструмента, описанного выше, мы можем осуществлить отбор нужного нам материала.