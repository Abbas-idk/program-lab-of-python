"""print in the format of 1/1 + 1/2 + 1/3 + ...... + 1/n"""
n=int(input('enter n value'))
sum_ = 0
for i in range(1,n+1):
    sum_ += 1/i
print(f"{sum_:.2f}")    
