class Solution:
    def longestPalindrome(self, s: str) -> str:        
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        ans = ""
        for i in range(len(s)):
            odd = expand(i, i)      # use i, not len(s)//2
            even = expand(i, i+1)   # use i, not len(s)//2
        # pick the longer one and update ans
            if len(odd) > len(ans):
                ans = odd
            if len(even) > len(ans):
                ans = even
        return ans