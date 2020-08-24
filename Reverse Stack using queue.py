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

