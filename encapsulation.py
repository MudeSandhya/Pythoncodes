#Encapusulation
#public encapsulation
class Public:
        def __init__(self,a):
                self.a=a
        def method(self):
                print(self.a)
obj=Public(2)
print(obj.a)
obj.method()
Public.method(obj)
#protector encapsulation
class protector:
        def __init__(self,a):
                self._a=a
        def method(self):
                print(self._a)
obj2=protector(200)
print(obj2._a)
obj2.method()
#private encapsulation
class private:
        def __init__(self):
                self.__a=200
        def method(self):
                print(self.__a)
objp=private()
#print(objp.__a)
#getter and setter to access private values and modify the value
class private:
        def __init__(self):
                self.__a=300
        def getter(self):
                return self.__a
        def setter(self):
                self.__a=int(input("enter the value:"))
objp=private()
print(objp.getter())
print(objp.setter())
print(objp.getter())
print(objp.__a)
                


        
        
       
