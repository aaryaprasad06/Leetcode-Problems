class Solution:
    def minLength(self, s: str) -> int:
        stack=[]
        top=-1
        for ch in s:
            if top==-1:
                stack.append(ch)
                top+=1
            else:
                if (ch=='B' and stack[top]=='A') or (ch=='D' and stack[top]=='C'):
                    stack.pop()
                    top-=1 
                else:
                    stack.append(ch)
                    top+=1 
        return len(stack)