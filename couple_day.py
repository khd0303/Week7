import datetime as dt

#first = dt.datetime(2021,1,3)
print ('처음으로 사귄 연도와 월, 일을 입력하시오')

year,month,day = map(int,input().split(' '))

first = dt.datetime(year,month,day)
hundred = dt.timedelta(days = 100)

date = first + hundred

print('100일 기념일은 : {}년 {}월 {}일 입니다'.format(date.year,date.month,date.day))