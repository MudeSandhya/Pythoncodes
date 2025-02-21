def SingleTonClass(arg):
    l=[]
    def inner():
        if len(l)==0:
            obj=arg()
            l.append(obj)
        return l[0]
    return inner
@SingleTonClass
class Movie1():
    def __init__(self):
        self.maxticks=100
    def Booking(self):
        print(f'available ticket is :{self.maxticks}')
        reqticks=int(input("enter the number of ticks:"))
        if reqticks<=self.maxticks:
            print("ticket booked successfully......")
            self.maxticks-=reqticks
        else:
            print("tickets not available")
@SingleTonClass
class movie2():
    def __init__(self):
        self.maxticks=300
    def Booking(self):
        print(f'available ticket is {self.maxticks}')
        reqticks=int(input("enter the tickets:"))
        if reqticks<=self.maxticks:
            print("ticket bookrd successfully")
            self.maxticks-=reqticks
        else:
            print("ticket not available")
@SingleTonClass
class movie3():
    def __init__(self):
        self.maxticks=150
    def Booking(self):
        print(f'available tickets {self.maxticks}')
        reqticks=int(input("enter the number of tickets:"))
        if reqticks<=self.maxticks:
            print("ticket bookrd successfully")
            self.maxticks-=reqticks
        else:
            print("ticket not available")
def bmys():
    print("1)movie1 \n2)movie2 \n3)movie3")
    option=int(input("enter the option movie"))
    if option==1:
        user=movie1()
        user.Booking()
    elif option==2:
        user=movie2()
        user.Booking()
    elif option==3:
        user=movie3()
        user.Booking()
    else:
        print("no movie available")
bmys()
print('-'*20)
bmys()
        

                     
    
