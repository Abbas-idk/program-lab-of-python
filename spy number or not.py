n=int(input('enter n value'))
sum_digits = 0
product_digits = 1
while n>0:
    r=n%10
    sum_digits+=r
    product_digits*=r
    n=n//10
if sum_digits == product_digits:
    print('spy number')
else:
    print('not a spy number')
