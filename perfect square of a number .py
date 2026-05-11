import math
n=int(input('enter n value'))
if n<0:
    print('negative numbers are not perfect square')
else:
    root=math.isqrt(n)
    if root*root==n:
        print(n,'is perfect square')
    else:
        print(n,'is not perfect square')
        
