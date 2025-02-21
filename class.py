'''class Bank():
    bank="axis"
    ROI=0.01
    def __init__(self,name,phno,adhar,pin,bal):
        self.name=name
        self.phno=phno
        self.adhar=adhar
        self.pin=pin
        self.bal=bal
    def balance(self):
        pin=int(input("enter the pin"))
        count=0
        if pin==self.pin:
            print(f'current balance is {self.bal}')
        else:
            if count<=3:
                print("wrong pin give crt pin")
                count+=1
    def deposit(self):
        amount=int(input("enter the deposit amount"))
        if amount<=20000:
            self.bal+=amount
            print(f'current balance {self.bal}')
        else:
            print("limit exits")
                   
obj1=Bank('sindhiya',7567876576,'ADHAR12345',1830,30000)
obj2=Bank('nikkal',9789869758,'ADGHAR4567',1803,12000)
obj1.balance()
obj2.deposit()
Bank.balanc(obj2)'''
class Bank1:
    bankname="sb"
    def __init__(self,name,phno,adhar,pin,bal):
        self.name=name
        self.phno=phno
        self.adhar=adhar
        self.pin=pin
        self.bal=bal
    def balance(self):
        count=0
        print("no of attempt count is 3")
        while count<3:
            if self.checkpin()==self.pin:
                print(f'current balance {self.bal}')
                break
            else:
                print("incorrect pin")
                print("try again")
                print(f'still {2-count} attempt ')
                count+=1
    @staticmethod
    def checkpin():
        count=0
        while count<3:
            passcode=int(input('enter the 4 digit pin:'))
            return passcode
    def deposit(self):
        count=0
        if self.checkpin()==self.pin:
            amount=int(input("Enter the deposit amount :"))
            if amount<=20000:
                self.bal+=amount
                print(f'available balanc{self.bal}')
            else:
                print("deposit amount is 20000 check te deposit amount")
        else:
            print("incorrect passwword...... try again")
            print("no of attemt is {3} still {2-count} is remaining")
            count+=1
    def withdraw(self):
        amount=int(input("enter the withdraw amount:"))
        if amount<=self.bal:
            count=0
            if self.checkpin()==self.pin:
                self.bal-=amount
                print("amount depeted succesfully")
                print(f'current balance {self.bal}')
            else:
                print("incorrect password...try again")
                print(f'check attemt {2-count}')
                count+=1
        else:
            print("insufficient Balance")
    @classmethod
    def alterclassname(cls):
        cls.bankname="state bank"
        print(bankname)

                
obj1=Bank1('sindhiya',7567876576,'ADHAR12345',1830,30000)
obj2=Bank1('nikkal',9789869758,'ADGHAR4567',1803,12000)
#obj1.balance()
#Bank1.deposit(obj1)
Bank1.withdraw(obj2)
Bank1.alterclassname()

                               
        
        
                     
              

