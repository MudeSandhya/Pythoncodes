class Bankv1:
    def __init__(self,name,mobno):
        self.name=name
        self.mobno=mobno
    def detail(self):
        print(f'name={self.name}')
        print(f'mobno={self.mobno}')
class Bankv2(Bankv1):
    def __init__(self,name,mobno,aadhar,pan):
        Bankv1.__init__(self,name,mobno)#class constructor
        self.aadhar=aadhar
        self.pan=pan
    def detail(self):
        super().detail()#super method class
        print(f'aadhar=self.aadhar')
        print(f'pan=self.pan')
class Bankv3(Bankv2):
    def __init__(self,name,mobno,aadhar,pan,accno,balance):
        super().__init__(name,mobno,aadhar,pan)#super class consructor
        self.accno=accno
        self.balance=balance
    def detail(self):
        super().detail()#supper method chaaining instand we can use the class method chain also
        print(f'accno=self.accno')
        print(f'balance=self.balance')
        
obj=Bankv3('sindhiya',7548819758,456437890345,'PANNOD1234','ADCERTUACNO456',20000)
print(obj.accno)
