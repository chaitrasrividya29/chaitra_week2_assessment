class bankemploye():
    def __init__(self,balance):
        self.balance=balance

    def deposit(self):
        self.depositamount=int(input("enter the amount to be deposited"))
        self.balance=self.depositamount + self.balance
        print("the amount in your is",self.balance)

    def withdraw(self):
        self.withdrawamount=int(input("enter the amount to be withdrawn"))
        self.balance= self.balance -self.withdrawamount
        print("the amount in your is",self.balance)

b=bankemploye(1000)
b.deposit()
b.withdraw()