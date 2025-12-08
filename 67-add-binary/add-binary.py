class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result=[]
        carry=0
        i= len(a)-1
        j= len(b)-1
        while i>=0 or j>=0 or carry:
            num1= int(a[i]) if i>=0 else 0
            num2= int(b[j]) if j>=0 else 0 
            total= num1 + num2 + carry 
            bit= total%2 
            carry= total//2
            result.append(str(bit))
            i-=1
            j-=1
        return "".join(result[::-1])