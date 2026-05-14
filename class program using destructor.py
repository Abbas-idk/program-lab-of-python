class Animal:
    def __init__(self,name):
        self.name=name
        print(f"object {self.name} is created")
    def __del__(self):
        print(f"{self.name} is destroying")
obj=Animal("dog")
del obj
