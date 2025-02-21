from abc import ABC,abstractmethod
class TV(ABC):
    @abstractmethod
    def news(self):
        pass
class sunnews(TV):
    def news(self):
        print("more over politics news will be run")
class instagram(TV):
    def news(self):
        print("all news will be there")
obj=instagram()
obj.news()

#concreate
class TV(ABC):
    def news(self):
        print("Tv channel news")
class sunnews(TV):
    def news(self):
        print("more over politics news will be run")
class instagram(TV):
    def news(self):
        print("all news will be there")
obj=TV()
obj.news()
