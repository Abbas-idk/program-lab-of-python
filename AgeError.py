class InvalidAgeError(Exception):
    def __init__(self,age,msg="Age should be >=0 and <=150"):
        self.age=age
        self.msg=msg
        super().__init__(self.msg)
def set_age(age):
    if(age<0 or age>150):
        raise InvalidAgeError(age)
    else:
        print(age)

try:
    set_age(12)
except InvalidAgeError as e:
    print(e)
