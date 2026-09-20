import os
from os import makedirs

from fontTools.misc.cython import returns

# os.mkdir('ne_folder')
makedirs(r"C:\Users\yulya\PycharmProjects\Lessoon_3\ne_folder\ne1\ne2", exist_ok=True)  # по
# машруту, гдн лежит папка folder я создаю новую папку ne. Это команда  exist_ok=True говорит,
# что если у меня это папка уже есть, то ничего делать не надо.
# Результат: в папке ne_folder появилась папка ne, ne1

# Далее создадим в этих папках текстовые файлы.
# with open(r"C:\Users\yulya\PycharmProjects\Lessoon_3\ne_folder\ne1\ne2\ne2.txt", 'w', encoding="utf-8") as file:
#     pass
# with open(r"C:\Users\yulya\PycharmProjects\Lessoon_3\ne_folder\ne1\ne2\ne2.py", 'w', encoding="utf-8") as file:
#     pass
# with open(r"C:\Users\yulya\PycharmProjects\Lessoon_3\ne_folder\ne1\ne1.txt", 'w', encoding="utf-8") as file:
#     pass
# with open(r"C:\Users\yulya\PycharmProjects\Lessoon_3\ne_folder\ne\ne1.py", 'w', encoding="utf-8") as file:
#     pass
# with open(r"C:\Users\yulya\PycharmProjects\Lessoon_3\ne_folder\base.txt", 'w', encoding="utf-8") as file:
#     pass


# ps = os.path.join(r"C:\Users\yulya\PycharmProjects\Lessoon_3\ne_folder", 'nnn')  # - join() 'это команда,
# # которая говорит какой машрут нужно создать.
# print(ps)
# Результат: образовался машрут "C:\Users\yulya\PycharmProjects\Lessoon_3\ne_folder\nnn" включая nnn.
# Благодаря join() туда записалась nnn.

# Есть другая команда:
# p = os.path.abspath('')  # Команда, которая говорит, где мы находимся.
# print(p)
# p = os.path.abspath(ps)
# print(p)
# Аналагичная запись:
# p = os.path.abspath('nnn')
# print(p)
# print(os.path.exists(p))  # Проверка, есть ли такая папка (р) или нет.
# Результат: False
# p = os.path.abspath('ne_folder')
# print(p)
# print(os.path.exists(p))  # Проверка, есть ли такая папка (р) или нет.
# Результат: True


def seek(target):
    size = 0  # размер
    folders = 0  # количество папок
    files = 0  # количество файлов
# Дальше должны понять где мы находимся:
    ps = os.path.join(target)
# Пропишем сам машрут:
    p = os.path.abspath(ps)
    for i in os.listdir(p):  # listdir(p) - это список директорий р
        # print(i)
        ps = os.path.join(p, i)
        if os.path.isfile(ps):
            size += os.path.getsize(ps)  # получаем размер файла ps
            files += 1
        else:
            folders += 1
            s, fs, f = seek(ps)
            size += s
            folders += fs
            files += f
    return size, folders, files

print(seek('ne_folder'))
