class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("Deposited:",amount)
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("Withdrawn:",amount)
        else:
            print("Insufficient balance")
    def display(self):
        print(self.name,"Balance:",self.balance)
#Real-time usage
acc1=BankAccount("Manoj",500000)
acc1.deposit(0)
acc1.withdraw(300000)
acc1.display()
