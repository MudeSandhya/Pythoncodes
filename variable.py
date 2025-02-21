#instance variable  and  class variable

class laptop:
    chargertype="B-type"#class variable that can defined for whote class variable
    def __init__(self):
        self.brand=""
        self.price=34
    def setprice(self,price):#instance method
        self.price=price
        
    def getprice(self):
        print(self.price)
    #@classmethod#decorator system that reads the class name without defing an class name in the setchargertype 
    def setchargertype(cls):#class method cls keyword for mention like self 
        cls.chargertype="B_Type"
        print("chargertype change to B")
    @staticmethod
    def info():
        print("it's an static method")
hp=laptop()
hp.setprice(20000)
hp.getprice()
laptop.setchargertype(laptop)
hp.info()
