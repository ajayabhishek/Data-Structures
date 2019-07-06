class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)

        if self.head is None:
            self.head=new_node
            return
        last_node=self.head
        while last_node.next is not None:
            last_node=last_node.next
        last_node.next=new_node

    def prepend(self,data):
        new_node=Node(data)

        new_node.next=self.head
        self.head=new_node

    def insert_after(self,prev_node,data):
        if not prev_node:
            print("Empty list")

        if prev_node.next is None:
            print("End of the list")

        new_node=Node(data)
        new_node.next=prev_node.next
        prev_node.next=new_node

    def delete(self,key):
        cur_node=self.head
        if cur_node and cur_node.data==key:
            self.head=code_node.next
            cur_node=None

        prev=None
        while cur_node and cur_node.data!=key:
            prev=cur_node
            cur_node=cur_node.next
            
        if cur_node is None:
            return
        prev.next=cur_node.next
        cur_node=None

    def delete_at_pos(self, pos):
        cur_node=self.head
        if pos==0:
            self.head=cur_node.next
            cur_node=None
            return
        
        prev=None
        count=1
        while cur_node and count !=pos:
            prev=cur_node
            cur_node=cur_node.next
            count +=1

        if cur_node is None:
            return
        prev.next=cur_node.next
        cur_node=None

    def counter(self):
        cur_node=self.head
        count=0
        while cur_node:
            count +=1
            cur_node=cur_node.next
        return count

    def swap(self,key1,key2):
        if key1==key2:
            return
        prev1=None
        cur1=self.head
        while cur1 and cur1.data!=key1:
            prev1=cur1
            cur1=cur1.next

        prev2=None
        cur2=self.head
        while cur2 and cur2.data!=key2:
            prev2=cur2
            cur2=cur2.next

        if not cur2 or not cur1:
            return

        if prev1:
            prev1.next=cur2
        else:
            self.head=cur2

        if prev2:
            prev2.next=cur1
        else:
            self.head=cur1

        cur1.next,cur2.next=cur2.next,cur1.next

    def print_help(self,node,name):
        if node is None:
            print(name+ ": None")
        else:
            print(name+":"+node.data)
            

    def reverse_stack(self):
        cur=self.head
        prev=None
        while cur is not None:
            nxt=cur.next
            cur.next=prev
            self.print_help(prev,"PREV:")
            self.print_help(cur,"CUR:")
            self.print_help(nxt,"NXT:")
            prev=cur
            cur=nxt
        self.head=prev

    def printlist(self):
        if self.head is None:
            print("Empty")
            return
        cur_node=self.head
        while cur_node:
            print(cur_node.data)
            cur_node=cur_node.next

ll=LinkedList()
ll.append("A")
ll.append("B")
ll.append("C")

#n=ll.head
#while ll.head.next.data is not "B":
#    ll.head=ll.head.next
#ll.insert_after(ll.head.next,"D")

ll.insert_after(ll.head.next,"E")

ll.prepend("Start")
ll.append("End")

#ll.delete_at_pos(4)
ll.swap("E","C") 
ll.printlist()
print(ll.counter())
ll.reverse_stack()
ll.printlist()
