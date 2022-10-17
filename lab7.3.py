import datetime as dt

now = dt.datetime.now()
thousand =  dt.timedelta(days = 1000)
nextday = now + thousand
print('1000일후 날짜 : {}년 {}월 {}일'.format(nextday.year,nextday.month,nextday.day))