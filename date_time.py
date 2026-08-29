from datetime import datetime, timedelta, date, time
# Все описанное выше - это разные типы данных. Python строго типизированный язык.
# И чтобы получить дату:
# d =date(2012, 10, 25)
# print(d, type(d))
# t = time(12, 15)
# print(t, type(t))
# # dt = d + t   # так будет ошибка
# dt = datetime.combine(d, t)
# print(dt, type(dt))
#
# # Получим текущее время:
# print(datetime.now())
# print(datetime.now().replace(microsecond= 0))  # результат без микросекунд
# ddt =datetime.now()
# ddt = ddt.replace(hour=12, minute=12, second=30, year=2025, month=1, day=1)
# print(ddt, type(ddt))  # превращение сегодняшнего числа в 2025 год в 01 месяц и т.д.
#
# # Задача: посчитать количество дней от какой-то даты.
# # Введем дату:
# # dat = input('введите дату (дд.мм.гггг):')
# # date_ =datetime.strptime(dat, '%d.%m.%Y')
# # print(date_)
#
# # Интересные методы:
# dt = datetime.now()
# # d = dt.timetuple()
# # for i in d:
# #     print(i)
# # Результат:
# # 2026 - год
# # 8 - месяц
# # 25 - число
# # 0 - часы
# # 51 - минуты
# # 11 - секунды
# # 1 - день недели (вторник). Начинается с понедельника и его значение = 0. Далее вторник - это 1, среда - это 2 и так далее.
# # 237 - отвечает на вопрос,какой это день в году.
# # -1 - говорит, что у нас нет перехода на зимнее/летнее время.
# print(dt.weekday()) # показывает день недели
# print(dt.isoweekday())
# cc =dt.isocalendar()
# print(cc)  # Результат: datetime.IsoCalendarDate(year=2026, week=35, weekday=2)
#
# print(dt.strftime("%A %B")) # %A - обозначает день недели, %B - обозначает месяц.
# days = ('Пн','Вт','Ср','Чт','Пт', 'Сб','Вс')
# print(days[dt.weekday()])
#
# # Понимание разницы между сегодняшней даты и той даты, которая была или которая будет.
# # Здесь этот момент важен (из чего что вычитать).
# dat = input('введите дату (дд.мм.гггг):')
# date_ =datetime.strptime(dat, '%d.%m.%Y')
# td = date_ - dt
# print(td)
# print(td.days)

# Задача про день рождение:

birthday = input('Дата рождения (дд.мм.гггг): ')  # ввели дату рождения
# Далее мы ее должны привести к международному формату (переопределением переменной birthday):
birthday = datetime.strptime(birthday, '%d.%m.%Y').date()
# Второй момент, который нам нужен это сегодняшний день:
date_today= date.today()
# print(birthday, date_today)
# Теперь нам надо сравнить эти две даты исходя из года, который идет сейчас и тем самым посчитать количество дней.
# Для этого нам надо получить год, который у нас сейчас.
year_ = date_today.year
birth_day = birthday
# Далее я беру birthday и в этот день перевожу
birthday = birthday.replace(year=year_)
age_days = (date_today - birth_day).days
# Теперь наша дата будет не 23.02.1997, а наша дата будет 23.02.2026
# print(birthday)
# Если дата рождения еще не наступила и она еще впереди, то мы можем написать:
# print(birthday - date_today)
# А если день рождение уже прошло и тогда прежде всего мы должны сравнить и сказать,
# если вдруг у нас birthdaу окажется меньше date_todaу то в этом случае мы выполним еще одну операцию:
# мы возьмем и нашему birthday = birthday.replace(year=year_) добавим year_+1. Т.е. присвоим еще тот год,который идет сейчас
if birthday < date_today:
    birthday = birthday.replace(year=year_ + 1)
    age_days = ((date_today + timedelta(days=365)) - birth_day).days
elif birthday == date_today:
    print('Поздравляем с Днем рождения!')
    exit(0)

days_ = (birthday - date_today).days
# age_days = (date_today - birth_day).days
# print(f'Количество дней до дня рождения - {days_} ')
# print(f'Количество дней до дня рождения - {}'.format(days_))
# print(f'Количество дней до дня рождения - %d'%{days_})

# Допишем сколько исполнится лет:

# Посчитаем количество лет:
# age = age_days // 365  # так писать неккоректно (делить нацело)
age = age_days / 365  # еще это выражение можно написать следующим образом и оно тоже будет верным: age = round(age_days // 365)
print(f'Количество дней до дня рождения - {days_}, Вам исполнится {age:.0f} лет ')









