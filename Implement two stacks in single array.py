class twoStacks:

    def __init__(self,n):

        self.size = n
        self.top1 = -1
        self.top2 = self.size
        self.arr = [None]*n

    def push1(self,x):
        if self.top1<self.top2-1:
            self.top1+=1
            self.arr[self.top1] = x

        else:
            print("Stack Overflow")
            exit(1)

    def push2(self,x):
        if self.top1<self.top2-1:
            self.top2-=1
            self.arr[self.top2] = x

        else:
            print("Stack Overflow")
            exit(1)

    def pop1(self):
        if self.top1>=0:
            x = self.arr[self.top1]
            self.top1-=1
            return x

        else:
            print("stack Underflow")
            exit(1)

    def pop2(self):
        if self.top2<self.size:
            x = self.arr[self.top2]
            self.top2+=1
            return x
        else:
            print("Stack Underflow")
            exit(1)

    
ts = twoStacks(5)
ts.push1('1')
ts.push1('2')
print("popped element from stack1 is", ts.pop1())
ts.push2('3')
ts.push2('4')
print("popped element from stack2 is", ts.pop2())
ts.push2('7')
print("popped element from stack2 is", ts.pop2())

print("popped element from stack2 is", ts.pop2())

print("popped element from stack2 is", ts.pop2())

