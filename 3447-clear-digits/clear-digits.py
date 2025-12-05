class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        top=-1
        s= list(s)
        for ch in s:
            if ch.isalpha():
                stack.append(ch)
                top+=1
            else:
                if stack[top].isalpha():
                    stack.pop()
                    top= top-1
        return "".join(stack)
            
