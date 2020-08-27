class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,x):
        return self.items.append(x)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    

def reverseString(string,stack):
    
    for i in range(len(string)):
        stack.push(string[i])

    while stack.isEmpty()==False:
        p = stack.top()
        stack.pop()
        print(p, end = "")


st = Stack()
reverseString('Hello I am Cool trends',st)

