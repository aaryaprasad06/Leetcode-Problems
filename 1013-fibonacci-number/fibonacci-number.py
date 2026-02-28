class Solution:
    def fib(self, n: int) -> int:
        if n==1 or n==2:
            return 1  
        a=0
        b=1
        c=0
        while n>1:
            c=a+b
            a=b
            b=c
            n-=1
        return c
        
        