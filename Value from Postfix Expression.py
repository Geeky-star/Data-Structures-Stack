
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

def postfix(string,stack):

    for i in string:
        if 48<=ord(i)<=57:
            stack.push(i)
        else:
            if stack.isEmpty()==False:
                p = stack.pop()
                q = stack.pop()
                p = int(p)
                q = int(q)
                if i=='+':
                    stack.push(p+q)
                if i=='-':
                    stack.push(q-p)
                if i=='/':
                    stack.push(q//p)

                if i=='*':
                    stack.push(p*q)

    print(stack.pop())

st = Stack()
postfix('138*+',st)
