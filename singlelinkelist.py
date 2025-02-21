class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class single_ll:
    def __init__(self):
        self.head = None
    def traverse(self):
        if self.head is None:
            print("single linklist is none")
        else:
            a=self.head
            while a is not None:
                print(a.data, end = ' ')
                a=a.next
            print()
    def insertatbeg(self, data):
        nb=Node(data)
        nb.next = self.head
        self.head = nb
    def insertatend(self,data):
        ne = Node(data)
        if self.head is None:
            self.head = ne
        else:
            a=self.head
            while a.next is not None:
                a = a.next
            a.next = ne
    def insertanyposition(self,data,poisition):
        nap=None(data)
        a=self.head
        for i in range(1,position-1):
            a=a.next
        nab.next=a.next
        a.next=nao
            
sll  = single_ll()
sll.insertatbeg(10)
sll.insertatbeg(20)
sll.insertatbeg(30)
sll.insertatbeg(40)
sll.insertatend(50)
sll.traverse()









