'''
class Stack:
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items==[]
    
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def top(self):
        return self.items[len(self.item)-1]
    
    def size(self):
        return len(self.items)
    
def deleteMid(stack,length,curr):
    
    if stack.isEmpty() or curr==length:
        return 
    
    x = stack.top()
    stack.pop()
    
    deleteMid(stack,length,curr+1)
    
    if curr == int(length)//2:
        stack.push(x)
        
st = Stack()
st.push('1')

st.push('2')

st.push('3')

st.push('4')

st.push('5')

st.push('6')

st.push('7')
        
deleteMid(st,st.size(),0)

while st.isEmpty()==False:
    p = st[st.size()-1]
    st.pop()
    print(p,end="\n")
    
'''


#construct in python
'''
class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items==[]

    def push(self,item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

st = Stack()
st.push("1")
st.push("2")
st.push("3")
st.push("4")
st.push("5")
st.push("6")
st.push("7")

while st.size()!=0:
    p = st.top()
    st.pop()
    print(p,end="\n")

'''

#Reverse stack using queue

'''
from queue import deque

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,x):
        return self.items.append(x)

    def top(self):
        return self.items[len(self.items)-1]

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def reverseStack(stack,n):
    queue = deque()
    if stack.isEmpty():
        return

    while stack.isEmpty()==False:
        x = stack.top()
        stack.pop()
        queue.append(x)
        

    while queue:
        x = queue.popleft()
        stack.push(x)


st = Stack()
st.push("1")
st.push("2")
st.push("3")
st.push("4")
st.push("5")
st.push("6")

print("stack before reversing")

while st.isEmpty()==False:
    p = st.top()
    st.pop()
    print(p, end="\n")

print("stack after reversing")

st = Stack()
st.push("1")
st.push("2")
st.push("3")
st.push("4")
st.push("5")
st.push("6")

reverseStack(st,st.size())

while st.isEmpty()==False:
    p = st.top()
    st.pop()
    print(p, end="\n")


'''

#Implement two Stacks in single array
'''
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

'''

#Reverse a string using Stack Data Structure
'''

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

'''

#Check if string of parenthesis is balanced or not
'''
class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,x):
        return self.items.append(x)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def top(self):
        return self.items[len(self.items)-1]


def checkBalanced(string,stack):

    for i in string:
        if i=='[' or i=='(' or i=='{':
            stack.push(i)

        
        if i==')' or i==']' or i=='}':
            if not stack:
                return False

            top = stack.pop()
            if (top=='(' and i!=')') or (top=='{' and i!='}') or (top=='[' and i!=']'):
                return False
            
    return True

st = Stack()

if checkBalanced("{()}[]",st)==True:
    print("string is balanced")

else:
    print("string is not balanced")

'''



#Reverse text without reversing individual words
'''
from collections import deque

class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,x):
        return self.items.append(x)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def top(self):
        return self.items[len(self.items)-1]


def reverseText(string,stack):
    low = 0
    high = 0

    for i in range(len(string)):
        if string[i]==" ":
            stack.push(string[low:high+1])
            low = i+1
            high = i+1

        else:
            high = i

    stack.push(string[low:])

    s = ''
    while stack.isEmpty()==False:
        s+=stack.pop()+ ' '

    return s[:-1]

st=Stack()
print(reverseText('We offer good placement',st))

'''

#Evaluate value of Postfix Expression
'''
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

'''

#Evaluate value of prefix Expression
'''
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

'''
'''
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

            
'''

#find minimum or maximum element from queue
'''
from queue import Queue
from collections import deque

class minMax:
  def enque_element(self,element):

    queue = Queue()
    dequ = deque()

    if queue.size()==0:
        queue.push(element)
        dequ.push_back(element)

    else:
        queue.push(element)

        while dequ and dequ>element:
            dequ.pop_back()

        dequ.push_back(element)



  def dequ_element():

    if queue.front() == dequ.front():
        queue.pop()
        dequ.pop_front()

    else:
        queue.pop()


  def getMin():
        return dequ.front()

k = minMax()
example = [1, 2, 4 ]
for i in range(3):
        k.enque_element(example[i])
    
print(k.getMin())


'''

class Stack:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def push(self,x):
        return self.items.append(x)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def validParenthesis(string,stack):
    
    for i in string:
        if i=='(' or i=='[' or i=='{':
            stack.push(i)

        else:
            if stack.isEmpty()==False:
                p=stack.top()
                if (p=='[' and i==']') or (p=='(' and i==')') or (p=='{' and i=='}'):
                    stack.pop()
                else:
                    stack.push(i)

            else:
                stack.push(i)


s=input()
st = Stack()
validParenthesis(s,st)
count = 0
while st.isEmpty()==False:
    p = st.top()
    st.pop()
    count+=1

print(count)


    





  
  






    










                
        


        
        


















    

















    




































