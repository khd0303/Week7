import datetime as dt

today = dt.date.today()
now = dt.datetime.now()

print('오늘의 날짜 : {}년 {} 월 {}일'.format(today.year,today.month,today.day))
if now.hour <= 12:
    print('현재시간 : 오전{}시 {}분 {}초'.format(now.hour,now.minute,now.second))
else:
    print('현재시간 : 오후 {}시 {}분 {}초'.format(now.hour-12,now.minute,now.second))