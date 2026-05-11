import math
n=int(input('enter n value'))
s = 0
temp = n
while n>0:
    r=n%10
    s=s+math.pow(r,3)
    n=n//10
if s==temp:
    print('Armstrong Number')
else:
    print('Not Armstrong Number')
