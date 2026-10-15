class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right= 0, 0
        seen= set()
        maxlen=0
        while left<=right and right != len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right+=1
            else:
                seen.remove(s[left])
                left+=1
            maxlen= max(maxlen, len(seen))
        return maxlen