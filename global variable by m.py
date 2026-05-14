a=23
def multiply():
    global a
    y=34
    a=a*y
    return a
print("New Value of a is",multiply())
print("Value of local variable y",y)
