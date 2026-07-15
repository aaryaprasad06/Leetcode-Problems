class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        if n==1:
            return 1
        oddsum=0
        evensum=0
        for i in range(1, 2*n+1):
            if i%2==0:
                evensum+=i
            else:
                oddsum+=i
        gcd=0
        for i in range(1, min(oddsum, evensum)):
            if oddsum%i==0 and evensum%i==0:
                gcd= i
        return gcd
