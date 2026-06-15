class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        top=-1
        op=['(', '{', '[']
        for char in s:
            if char in op:
                stack.append(char)
                top+=1
            else:
                if top < 0:
                    return False
                if (stack[top]=='(' and char==')') or (stack[top]=='[' and char==']') or (stack[top]=='{' and char=='}'):
                    stack.pop()
                    top-=1
                else:
                    return False
        if len(stack)!=0:
            return False
        else:
            return True
            
        