duration = int(input("Введите количество секунд: "))

min = 60
hour = min * 60
day = hour * 24

if duration <= 60:
    print(duration, "сек")
elif duration > 60 and duration <= hour:
    result_min = duration // min
    result_sec = duration % min
    print(result_min, 'мин.', result_sec, 'сек')
elif duration > hour and duration < day:
    result_hour = duration // hour
    result_min = duration % hour // min
    result_sec = duration % result_min
    print(result_hour, 'час.', result_min, 'мин', result_sec, 'сек')
else:
    result_day = duration // day
    result_hour = duration % day // hour
    result_min = duration % hour // min
    result_sec = duration % min
    print(result_day, 'дн.', result_hour, 'час.', result_min, 'мин.', result_sec, 'сек.')

