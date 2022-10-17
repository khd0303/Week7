import math as m


#1

for i in range(2,11):
    print('4**',i,'=',m.pow(4,i))


print()

print()

#2

for i in range(0,181,10):
    print(i,'degree = ',round(m.radians(i),3),'radian')
print()
print()


#3
for i in range(0,181,10):
   print('sin({}) = {}'.format(i,round(m.sin(m.pi *(i/180) ),2)))
