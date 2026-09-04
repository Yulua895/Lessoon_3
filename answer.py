import random
import time

from декараторы import time_run, null, in_out


# l = random.sample(range(0, 1000000), 1000000)
# ll = l.copy()
# # null()
#
# # Сравним два метода: 1-ый преобразование нашего списка в строку.
# # Для этого есть два способа:
#
# # Декаратор вешается на какую-либо функцию поэтому ее пропишем ниже:
# @time_run
# def r1():
#     res1 = list(map(str, l))
#     print(res1[:5])
#
#
# @time_run
# def r2():
#     res2 = [str(i) for i in ll]
#     print(res2[:5])
#
#
# r1()
# r2()
# res1 = list(map(str, l))  # res1 это список, который порождается от генератора map.
# res2 = [str(i) for i in ll]

# @time_run
# def etalon(n):
#     print('START')
#     time.sleep(n)
#     print('END')
#
# etalon(3)


@time_run
def etalon(n, m, x=4):  # n и m - это позиционные аргументы.
    # x=4 - это ключевой аргумент (у которых есть ключ/значение)
    print('START')
    time.sleep(n+m)
    print(x)

# etalon(3, 1, x=10)

@in_out
def summer(x, y):
    return x + y


res = summer(random.randint(1, 100),
             random.randint(1, 100)) / 3.45 ** 3
print(res)