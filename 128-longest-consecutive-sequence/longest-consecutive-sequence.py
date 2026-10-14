class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums)==0:
            return 0
        
        unique= set(nums)
        lcs=0
        for i in unique:
            if i-1 in unique:
                continue
            count=1 
            while i+count in unique:
                count+=1 
            if count> lcs:
                lcs= count 
        return lcs