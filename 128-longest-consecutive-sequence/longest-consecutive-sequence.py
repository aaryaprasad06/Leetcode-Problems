class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        ans= 0
        unique= set(nums)
        if len(nums)==0:
            return 0
        for n in (unique):
            if n-1 in unique:
                continue 
            else:
                count=1 
                while n+count in unique:
                    count+=1 
                ans= max(ans, count)
        return ans