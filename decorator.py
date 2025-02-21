def outer(args):
    print("bye")
    def inner():
        obj=args()
    return inner
@outer
class m17():
    def __init__(self):
        print("constructor is created")
m17()
m17()
