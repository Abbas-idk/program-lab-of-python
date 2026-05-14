class AgetoVoteError(Exception):
    def __init__(self,age,msg="Age should be >= 18"):
        self.age=age
        self.msg=msg
        super().__init__(self.msg)
def set_age(age):
    if(age<18):
        raise AgetoVoteError(age)
    else:
        print(age)
try:
    set_age(12)
except AgetoVoteError as e:
    print(e)
