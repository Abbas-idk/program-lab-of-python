class Product:
    def __init__(self,name,base_price,stock):
        self.name=name
        self.base_price=base_price
        self.stock=stock
    def get_price(self):
        if self.stock<10:
            return self.base_price * 1.2
        elif self.stock<=50:
            return self.base_price
        else:
            return self.base_price * 0.9
    def update_stock(self,quantity):
        if self.stock + quantity < 0:
            print("Not enough stock available!")
        else:
            self.stock += quantity
            print("Stock updated. Current stock: (self.stock)")
    def display(self):
        print(f"Product: {self.name}")
        print(f"Stock: {self.stock}")
        print(f"Current Price: ${self.get_price():.2f}")
        print("-"*30)
