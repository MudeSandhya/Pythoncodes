class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
    def forward_DLL(self):
        if self.head is None:
            print("double link list is empty")
        else:
            a=self.head
            while a is not None:
                print(a.data,end=' ')
                a=a.next
    def backwardtraversal(self):
        print()
        if self.head is None:
            print('double link list is empty')
        else:
            a=self.head
            while a.next is not None:
                a=a.next
            while a is not None:
                print(a.data,end=' ')
                a=a.prev
    def insert_at_beginning(self,data):
        print()
        ns=node(data)
        a=self.head
        a.prev=ns
        ns.next=a
        self.head=ns
    def insert_at_End(self,data):
        print()
        ne=node(data)
        a=self.head
        while a.next is not None:
            a=a.next
        a.next=ne
        ne.prev=a
    def insert_at_specificpos(self,position,data):
        print()
        ns=node(data)
        a=self.head
        for i in range(1,position-1):
            a=a.next
        ns.prev=a
        ns.next=a.next
        a.next.prev=ns
        a.next=ne
    def delete
n1=node(5)
dll=dll()
dll.head=n1
n2=node(10)
n2.prev=n1
n1.next=n2
n3=node(30)
n3.prev=n2
n2.next=n3
n4=node(40)
n4.prev=n3
n3.next=n4
dll.forward_DLL()
dll.backwardtraversal()
dll.insert_at_beginning(3)
dll.forward_DLL()
dll.backwardtraversal()
dll.insert_at_End(50)
dll.forward_DLL()
dll.backwardtraversal()
dll.insert_at_specificpos(3,7)
dll.forward_DLL()
dll.backwardtraversal()

                
