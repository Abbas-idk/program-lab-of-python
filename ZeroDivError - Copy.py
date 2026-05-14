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

#Type Error
try:
    a=12+"10"
except TypeError:
    print("give correct data types")
else:
    print(a)
finally:
    print("Program completed")

l=[90,"ten",40]
try:
    a=l[0]+int(l[1])
except ValueError:
    print("give numbers only")
else:
    print(a)
finally:
    print("program completed")
