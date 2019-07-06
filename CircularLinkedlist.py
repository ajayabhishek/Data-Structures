class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CircularLinkedlist:
    def __init__(self):
        self.head=None

    def append(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            self.head.next=self.head
        else:
            cur=self.head
            while cur.next!=self.head:
                cur=cur.next
            cur.next=new
            new.next=self.head

    def prepend(self,data):
        new=Node(data)
        new.next=self.head
        cur=self.head

        if self.head is None:
            self.head=new
            self.head.next=self.head

        else:
            while cur.next!=self.head:
                cur=cur.next
            cur.next=new
            self.head=new

    def delete(self,key):
        cur=self.head
        prev=None

        if self.head.data==key:
            cur=self.head
            while cur.next!=self.head:
                cur=cur.next
            cur.next=self.head.next
            self.head=self.head.next
        else:
            while cur.next!=self.head:
                prev=cur
                cur=cur.next
                if cur.data==key:
                    prev.next=cur.next
                    cur=cur.next
                    
            
    def isCircular(self,linkedlist):
        cur=linkedlist.head
        while cur.next:
            cur=cur.next
            if cur.next==linkedlist.head:
                return True
        return False
                
            
        if count>0:
            print("yes")

    def print_list(self):
        cur=self.head
        while cur:
            print(cur.data)
            cur=cur.next
            if cur==self.head:
                break

clink=CircularLinkedlist()
clink.append("A")
clink.append("B")
clink.append("XX")
clink.append("C")
clink.append("D")
clink.prepend("Start")
clink.prepend("XX")
clink.append("End")
clink.print_list()
print("Removing all XX")
clink.delete("XX")
clink.delete("XX")
clink.print_list()
print(clink.isCircular(clink))
