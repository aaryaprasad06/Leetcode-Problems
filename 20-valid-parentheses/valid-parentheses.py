class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        top=0
        s= list(s)
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='{' or s[i]== '[':
                stack.append(s[i])
                top+=1
            else:
                if top==0:
                    return False
                if (s[i]==')' and stack[top-1]=='(') or (s[i]==']' and stack[top-1]=='[') or (s[i]=='}' and stack[top-1]=='{'):
                    stack.pop()
                    top-=1 
                else:
                    return False
                
        
        if top==0:
            return True
        else:
            return False
        