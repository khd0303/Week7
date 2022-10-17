import datetime as dt
#1
today = dt.date.today()

print('오늘은 {}년 {} 월 {}일 입니다'.format(today.year,today.month,today.day))

xmas = dt.datetime(2025,12,25)

timegap = xmas - dt.datetime.now()

print('다음 크리스마스 까지는 {}일 {}시간 남았습니다'.format(timegap.days,timegap.seconds //3600))

#2

today = dt.date.today()

print('오늘은 {}년 {} 월 {}일 입니다'.format(today.year,today.month,today.day))

newyear = dt.datetime(2036,1,1)

timegap = newyear - dt.datetime.now()

print('다음 새해 까지는 {}일 {}시간 남았습니다'.format(timegap.days,timegap.seconds //3600))

#3
today = dt.date.today()

print('오늘은 {}년 {} 월 {}일 입니다'.format(today.year,today.month,today.day))

birthday = dt.datetime(2023,3,3)

timegap = birthday - dt.datetime.now()

print('다음 생일 까지는 {}일 {}시간 남았습니다'.format(timegap.days,timegap.seconds //3600))