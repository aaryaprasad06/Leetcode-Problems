class MinStack:

    def __init__(self):
        self.stack=[]
        self.minval=[]

    def push(self, value: int) -> None:
        self.stack.append(value)
        if len(self.minval)==0:
            self.minval.append(value)
        else:
            self.minval.append(min(self.minval[-1], value))
        
    def pop(self) -> None:
        self.minval.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minval[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()