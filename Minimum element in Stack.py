class MinStack:

    def __init__(self):
        self.stack = []
        self.min_curr = float("inf")
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        
        if x<self.min_curr:
            self.min_curr = x
        

    def pop(self) -> None:
        del self.stack[-1]
        if len(self.stack):
            self.min_curr = min(self.stack)
        else:
            self.min_curr = float("inf")
            
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.min_curr
        
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
