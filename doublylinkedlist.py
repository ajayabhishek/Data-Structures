class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class doublylinkedList():
    def __init__(self):
        self.head=None

    def append(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            new.prev=None
        else:
            cur=self.head
            while cur.next:
                cur=cur.next
            cur.next=new
            new.prev=cur
            new.next=None
    def prepend(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            new.prev=None
        else:
            new.next=self.head
            self.head=new
            new.prev=None

    def add_before(self,key,data):
        cur=self.head
        while cur:
            if cur.prev is None and cur.data==key:
                self.prepend(data)
                return
            elif cur.data==key:
                new=Node(data)
                p=cur.prev
                p.next=new
                new.next=cur
                new.prev=p
                cur.prev=new            
            cur=cur.next

    def add_after(self,key,data):
        cur=self.head
        while cur:
            if cur.next is None and cur.data==key:
                self.append(data)
                return
            elif cur.data==key:
                new=Node(data)
                nxt=cur.next
                cur.next=new
                new.next=nxt
                new.prev=cur
                nxt.prev=new
            cur=cur.next
        
        

    def printlist(self):
        cur=self.head
        while cur:
            print(cur.data)
            cur=cur.next

dlist=doublylinkedList()
dlist.append(1)
dlist.append(2)
dlist.append(3)
dlist.append(4)
dlist.append(5)
dlist.append("End")
dlist.prepend("Start")
dlist.add_before(4,"Three")
dlist.add_after(5,"Five")
dlist.printlist()
                
