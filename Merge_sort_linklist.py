class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return

        cur=self.head
        while cur.next is not None:
            cur=cur.next
        cur.next=new_node

    def counter(self):
        cur=self.head
        count=0
        while cur:
            count +=1
            cur=cur.next
        return count

    def merge_sort(self,llist):
        p=self.head
        q=llist.head
        s=None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data<=q.data:
                s=p
                p=s.next
            else:
                s=q
                q=s.next
            new_head=s
        while p and q:
            if p.data<=q.data:
                s.next=p
                s=p
                p=s.next
            else:
                s.next=q
                s=q
                q=s.next

        if not p:
            s.next=q
        if not q:
            s.next=p
        return new_head

    def remove_duplicates(self):
        prev=None
        cur=self.head
        dups=dict()

        while cur:
            if cur.data in dups:
                prev.next=cur.next
                cur=None

            else:
                dups[cur.data]=1
                prev=cur
            cur=prev.next

    def get_nth_from_last(self,n):
        length=self.counter()
        cur=self.head
        while cur:
            if length is n:
                print(n,"number from last is:-")
                print(cur.data)
                return cur
            length=length-1
            cur=cur.next
        if cur is None:
            return
    

    def occurences(self,data):
        count=0
        cur=self.head

        while cur:
            if cur.data==data:
                count +=1
                
            cur=cur.next
        return count

    def rotate(self,k):
        prev=None
        q=self.head
        p=self.head
        count=0
        while p and count<k:
            prev=p
            p=p.next
            #q=q.next
            count+=1
        p=prev
        
        while q:
            prev=q
            q=q.next
            
        q=prev
        q.next=self.head
        self.head=p.next
        p.next=None

    
    def printlist(self):
        cur=self.head
        while cur is not None:
            print(cur.data)
            cur=cur.next

ll1=Linkedlist()
ll2=Linkedlist()


ll1.append(1)
ll1.append(5)
ll1.append(7)
ll1.append(9)
ll1.append(10)

ll2.append(2)
ll2.append(3)
ll2.append(4)
ll2.append(6)
#ll2.append(6)
ll2.append(8)

ll1.merge_sort(ll2)

#ll1.remove_duplicates()
ll1.printlist()

#ll1.get_nth_from_last(2)
#print(ll1.occurences(6))
print("Rotated list is")
ll1.rotate(7)
ll1.printlist()            
