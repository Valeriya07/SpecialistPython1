# Напишите функцию принимающую время в секундах и возвращающую строку формата: “hh:mm:ss”,
# где hh - часы, mm- минуты, ss - секунды.
# Пример:
# 29143 секунд → 08:05:43

import datetime


def date_time(t):
    return str(datetime.timedelta(seconds=t))


print(date_time(29143))
