class father:
    def __init__(self):
        self.dadmoney=0    
    def money(self,dadmoney):
        self.dadmoney=dadmoney
        return dadmoney
class mother:
    def __init__(self):
        self.mommoney=0
    def money(self,mommoney):
        self.mommoney=mommoney
class child(father,mother):
    def __init__(self):
        super().__init__()
    def calculate(self,dadmoney,mommoney):
        self.money(dadmoney)
        mother.money(self,mommoney)
        amount=int(input("enter the amount acc balance:"))
        if amount<150:
            self.dadmoney+=amount
            if self.dadmoney>150:
                print(self.dadmoney)
            else:
                amount+=self.mommoney
        else:
            print("stop plan and go and study")
obj=child()
dadmoney,mommoney=int(input("enter the dad amount")),int(input("enter the moms money"))
obj.calculate(dadmoney,mommoney)
        
            
        
        
