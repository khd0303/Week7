#1
'''
import random as rd
num1 = rd.randint(1, 6)

num2 = rd.randint(1, 6)

print('로미오의 주사위 숫자는 : {}입니다 \n줄리엣의 주사위 숫자는 : {} 입니다'.format(num1, num2))

if num1 > num2:
    print('로미오가 이겼습니다')
elif num2 > num1:
    print('줄리엣이 이겼습니다')
else:
    print('비겼습니다')
'''
'''
#2
import random as rd
answer = rd.randint(1,21)
count = 1

#print(answer)
while(1):
    num = int(input('1~20사이의 숫자를 입력하시오 : '))
    if num > answer:
        print('{}보다 큽니다'.format(answer))
        count +=1
    elif num < answer:
        print('{}보다 작습니다'.format(answer))
        count +=1
    else:

        print('정답입니다')
        if(count <=3):
            print('{}번만에 맞춘 당신은 천재'.format(count))

        elif(count >3 & count <=6):
            print('{}번만에 맞추셨군요 잘했어요'.format(count))
        else:
            print('{}번만에 맞추다니 쩝쩝'.format(count))

        break
'''

'''
#3

import turtle as t
t.color('blue')
t.circle(50)

t.setheading(-45)
t.color('yellow')
t.circle(50)

'''
#6
import datetime

today = datetime.datetime.today()

print('오늘은 {}년 {}월 {}일 입니다'.format(today.year,today.month,today.day))

firstday = datetime.datetime(2019,2,14)
print('춘향이와 몽룡이의 연애시작일 : {}년 {}월 {}일'.format(firstday.year,firstday.month,firstday.day))
gap1 = today - firstday
print('연애시작일부터 경과한 날짜 {}일'.format(gap1.days))

hundered = datetime.timedelta(days = 100)
thundred = datetime.timedelta(days = 200)
fhundred = datetime.timedelta(days = 500)
thousand = datetime.timedelta(days = 1000)

print('100일 경과일 : {}년 {}월 {}일'.format((firstday + hundered).year,(firstday + hundered).month,(firstday + hundered).day))
print('200일 경과일 : {}년 {}월 {}일'.format((firstday + thundred).year,(firstday + thundred).month,(firstday + thundred).day))
print('500일 경과일 : {}년 {}월 {}일'.format((firstday + fhundred).year,(firstday + fhundred).month,(firstday + fhundred).day))
print('1000일 경과일 : {}년 {}월 {}일'.format((firstday + thousand).year,(firstday + thousand).month,(firstday + thousand).day))

'''
#7

import time as t
def sum1to1000000():
    result = 0
    for i in range(1,1000001):
        result += i



start_time = t.time()

for i in range(100):
    sum1to1000000()



result_time = t.time()


gap = result_time - start_time

print('1에서 100만까지의 합을 100번 반복해서 구하는 시간 : {:7.4f}초'.format(gap))
'''



#8

#(1)
'''
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(' factorial 1000 :  {}'.format(factorial(1000)))
'''
#결과 값이 너무 커서 파이참 내부에서 실행할수 없음   작은 수를 넣으면 정상적으로 작동됨

'''
#(2)

import time
def multodd(n):
    result = 0

    for i in range(n):
        if i % 2 == 1:
            result += i ** 3

    return result


print('1부터 1000까지의 홀수를 세제곱 더하기 결과 :',multodd(1001))

first = time.time()

for i in range(100):
    multodd(1001)

end = time.time()

gap = end - first

print('1에서 1000까지의 홀수의 세제곱 더하기를 100번 반복하는 시간 : {:7.4f}초'.format(gap))
'''


#(3)
'''
import time
import math as m

def sin(n):
    result = 0
    for i in range(1, n):
        result += m.sin(m.pi * (i / 180))
        # print('sin(',i,')',m.sin(m.pi * (i / 180)))
    return result





print('1에서 360도 까지의 sin값의 합:',sin(361))

first = time.time()

for i in range(100):
    sin(361)
end = time.time()
gap = end - first
print('1에서 360도 까지의 sin 더하기를 100번 반복하는 시간 : {:7.4f}초'.format(gap))
'''

'''
#9

import random as r

def myRand():
    for i in range(10):

        print(r.randint(0,1000000))


myRand()
'''