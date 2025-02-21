class bank():
    def __init__(self,bal):
        self.bal=bal
    def deposit(self):
        amount=int(input("enter the amount:"))
        self.bal+=amount
        print(f"available balance amount{self.bal}")
class paytm(bank):
    def __init__(self,bal):
        self.bal=bal
obj=paytm(1000)
obj.deposit()
