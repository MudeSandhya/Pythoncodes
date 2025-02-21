class animal():
    def sound(self):
        print("animal makes a sound")
class dog(animal):
    def __init__(self):
        print("dog barks")
class bird(animal):
    def __init__(self):
        super().__init__()
        print("birds sing")
o=bird()
