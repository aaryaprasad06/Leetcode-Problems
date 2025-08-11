class Solution:
    def isHappy(self, n: int) -> bool:
        n= self.Add(n)
        while (n>1 and n!=4):
            n=self.Add(n)
        return n==1

    def Add(self, num):
        sum=0
        while num>0:
            a= num%10
            sum= sum+ (a*a)
            num= num//10
        return sum