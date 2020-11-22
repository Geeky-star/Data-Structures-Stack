class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, x):
        return self.items.append(x)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def top(self):
        return self.items[-1]


st = Stack()
for i in range(len(arr)):
    

    if st.isEmpty()==True:
        l.append(-1)
        st.push(arr[i])

    if st.top()<arr[i]:
        l.append(st.top())

    elif st.top()>arr[i]:

        while st.isEmpty()==False and st.top()>arr[i]:

            st.pop()

        if st.isEmpty()==False:
                 l.append(st.top())

        else:
            l.append(-1)
            st.push(arr[i])
            
     

print(l)

