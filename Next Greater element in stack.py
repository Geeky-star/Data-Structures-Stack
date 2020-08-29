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


def nxtgreater(array,stack):
    if stack.isEmpty():
        stack.push(array[0])

    for i in array:
        x=i
        if x>int(stack.top()):
            print('next greater element of ',stack.top(), 'is', x)
            stack.push(x)
           
        

st = Stack()
array = [3,7,1,9]
nxtgreater(array,st)

