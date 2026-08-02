class Solution:
    def myAtoi(self, s: str) -> int:
        s= s.lstrip()
        s= s.rstrip()

        if not s:
            return 0

        sign= 1
        ptr=0
        num=0

        if s[ptr] =='-':
            sign= -1 
            ptr+=1
        elif s[ptr]=='+':
            ptr+=1 
        
        while ptr< len(s):
            if not s[ptr].isdigit():
                break 
            num= (num*10)+ int(s[ptr])
            ptr+=1 

        num= num*sign

        if num> 2**31-1:
            num= 2**31-1
        if num< -2**31:
            num= -2**31 
        
        return num