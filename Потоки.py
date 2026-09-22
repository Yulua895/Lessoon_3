# Выполнение модуля - это процесс.
# И в этом процессе идет какой-то поток информации на процесс.
# Грубо говоря работа модуля - это процесс, а процессия есть поток.
# Поток - это единица выполнения внутри процесса.

# Потоки - это дополнительные какие-то паралельные действия , связанные с вводом и выводом
# информации (файлом, перекачкой файла, перекачкой в интернет, на сайте и т.д.). Потоки -
# это когда что-то делается не одновременно (разложение по полочкам), а паралельно.

import time
from time import sleep
from threading import Thread

from декараторы import time_run


class WorkThread(Thread):  # класс рабочий паток
    def __init__(self, num, tab, vol, dur):
        super().__init__()
        self.num = num
        self.tab = tab
        self.vol = vol
        self.dur = dur


    def run(self):# сама функция определяется методом run
        print(f'Поток {self.num} started')  # self.num - это номер патока
        for k in range(self.vol):
            print(f'{self.tab} Поток {self.num} -> Действие № {k + 1}')
            sleep(self.dur)
        print(f'Поток {self.num} stopped')




def f1(n):
    print(n ** 2)
    time.sleep(3)  # сделали имитацию задержки
    print('f1 completed')


def f2(n):
    print(n * 2)
    time.sleep(2)
    print('f2 completed')

@time_run
def main():  # запускает
    # f1(5)
    # f2(50)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

if __name__ == '__main__':
    thread1 = Thread(target=f1, args=(5,))  # это дополнительный поток
    thread2 = Thread(target=f1, args=(50,))  # это дополнительный поток

    main()  # это основной поток


