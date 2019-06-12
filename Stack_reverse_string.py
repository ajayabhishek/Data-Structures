class Stack:
    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items==[]

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

    def get_stack(self):
        return self.items
def rev_string(stack,input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])

    rev_str=""
    while not stack.isEmpty():
        rev_str +=stack.pop()
    return rev_str
stack=Stack()
input_str="Hello"
print(rev_string(stack,input_str))
    
