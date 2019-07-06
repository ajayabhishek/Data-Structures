class Node:
    def __init__(self,data):
        self.next=None
        self.data=data

class Linkedlist:
    def __init__(self):
        self.head=None

    def append(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            return
        cur=self.head
        while cur.next is not None:
            cur=cur.next
        cur.next=new

    def is_pallindrome(self):
        cur=self.head
        s=""
        while cur:
            s+=cur.data
            cur=cur.next
        if s==s[::-1]:
            print("Is pallindrome")
        else:
            print("Is not pallindrome")

    def last_to_head(self):
        cur=self.head
        prev=None
        while cur.next:
            prev=cur
            cur=cur.next
        cur.next=self.head
        self.head=cur
        prev.next=None

        
    def printlist(self):
        cur=self.head
        while cur:
            print(cur.data)
            cur=cur.next


list1=Linkedlist()
list1.append("R")
list1.append("A")
list1.append("D")
list1.append("A")
list1.append("R")
list1.printlist()
list1.is_pallindrome()
list1.last_to_head()
list1.printlist()
