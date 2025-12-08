class Solution:
    def romanToInt(self, s: str) -> int:
        d={
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        s= list(s)
        total= 0
        for i in range(len(s)-1):
            curr_val= d[s[i]]
            next_val= d[s[i+1]]
            if curr_val < next_val:
                total -= curr_val
            else:
                total+= curr_val 
        total+= d[s[-1]]
        return total