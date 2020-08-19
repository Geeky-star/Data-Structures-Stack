
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
        return self.items[len(self.items)-1]
    
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

st.push('9')

st.push('5')

        
deleteMid(st,st.size(),0)

while st.isEmpty()==False:
    p = st.top()
    st.pop()
    print(p,end="\n")
