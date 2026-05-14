try:
    a=78
    b=0
    c=a/b
except ZeroDivisionError:
    print("dividing by zero")
else:
    print(c)
finally:
    print("Program completed")

#Value Error
try:
    a=int("ten")
except ValueError:
    print("give numbers only")
else:
    print(a)
finally:
    print("Program completed")
