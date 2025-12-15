class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        sol=[]
        for i in range(left, right+1):
            temp=i
            while temp!=0:
                a= temp%10 
                if a!=0 and i%a==0:
                    temp= temp//10 
                else:
                    break 
            if temp==0:
                sol.append(i)
        return sol