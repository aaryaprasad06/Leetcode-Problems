class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        opened= {'[', '(', '{'}
        for ch in s:
            if ch in opened:
                stack.append(ch)
            else:
                if len(stack)==0:
                    return False 
                else:
                    if (ch==']' and stack[-1]=='[') or (ch=='}' and stack[-1]=='{') or (ch==')' and stack[-1]=='('):
                        stack.pop() 
                    else:
                        return False 
        if len(stack)==0:
            return True
        else:
            return False