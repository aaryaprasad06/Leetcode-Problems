class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        top=-1
        for ch in s:
            if top==-1:
                stack.append(ch)
                top+=1 
            else:
                if (ord(stack[top])- 32== ord(ch)) or (ord(stack[top])+ 32== ord(ch)):
                    stack.pop()
                    top-=1
                else:
                    stack.append(ch)
                    top+=1 
        return "".join(stack)