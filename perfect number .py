n=int(input('enter n value'))
div_sum=0
if n<0:
    print('negative numbers are not perfect numbers')
else:
    for i in range(1,n):
        if n%i==0:
            div_sum+=i
if div_sum==n:
    print(n,'is perfect number')
else:
    print(n,'is not perfect number')
