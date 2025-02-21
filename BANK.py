class bank:
    bname="AXIS"
    roi=0.01
    def __init__(self, name, phno, accno,aadhar, pan, pin, bal):
        self.name = name
        self.phno = phno
        self.accno = accno
        self.aadhar = aadhar
        self.pan = pan
        self.pin = pin
        self.bal = bal
    def balcheck(self):
        count=0
        print("total number of attemt 3")
        while count<3:
            if self.checkpin() == self.pin:
                print(f'available bal {self.bal}')
                break
            else:
                print('Try again')
                print(f'remaining attem is {2-count}')
        else:
            print("Failed to many times.access denied")
    @staticmethod
    def checkpin():
        count=0
        print("total no of attempt is 3")
        while count<3:
            passcode=int(input("enter the password"))
            return passcode
    def deposit(self):
            count=0
            amount=int(input("enter the amount:"))
            if amount<20000:
                self.bal+=amount
                print("amount cretided successfully")
                print("accountbalance {self.bal}")
            else:
                print("max amount deposit is 20000")
    def withdraw(self):
        count=0
        while count < 3:
            print("number of attempt is 3")
            if self.checkpin()== self.pin:
                amount=int(input("enter the  amount"))
                if amount<=20000:
                    if self.bal>= amount:
                        self.bal-=amount
                        print("succesfully withdrawn the amount")
                        print(f'available balance {self.bal}')
                    else:
                        print("insufficient amount")       
                else:
                    print("withdraw amount limit is less than 20000")
            else:
                count+=1
                print("withdraw amount limit is less than 20000")
            break
        else:
            print("Failed too many times. Withdrawl denied.")
   @classmethod
   def alterbankname(cls):
       cls.bname = "State Bank of India"
       print(f"Bank name updated to: {cls.bname}")dx

user1= bank("sandhya",7548819758,"AC40UCS34567",'ADHAR1234234','PANNUMBER1',181630,10000)
user2= bank("sandhya",7548869758,"AC40UCS34568",'ADHAR12349834','PANNUMBER2',181631,1000)
user2.deposit()
    

        
            
            
            
