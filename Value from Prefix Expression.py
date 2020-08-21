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


def prefix(string,stack1,stack2):

    for i in string:
        stack1.push(i)

    while stack1.isEmpty()==False:
        a = stack1.pop()
        if 48<=ord(a)<=57:
            stack2.push(a)
        else:
            p = stack2.pop()
            q = stack2.pop()
            p = int(p)
            q = int(q)
            if a=='+':
                stack2.push(p+q)

            if a=='-':
                stack2.push(p-q)

            if a=='/':
                stack2.push(q//p)

            if a=='*':
                stack2.push(p*q)

    print(stack2.pop())

st1 = Stack()
st2 = Stack()
prefix('-+8/632',st1,st2)
