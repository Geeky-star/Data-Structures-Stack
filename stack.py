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


    





  
  






    










                
        


        
        


















    

















    




































