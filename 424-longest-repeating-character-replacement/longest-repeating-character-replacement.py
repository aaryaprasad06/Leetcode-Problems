class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        occurence=[0]*26
        left=0
        right=0
        ans=0 
        maxfreq=0

        for right in range(len(s)):
            occurence[ord(s[right])-ord('A')]+=1
            maxfreq= max(maxfreq, occurence[ord(s[right])- ord('A')])

            if right-left+1- maxfreq >k:
                occurence[ord(s[left])-ord('A')]-=1 
                left+=1
            ans= max(ans, right-left+1)
        return ans