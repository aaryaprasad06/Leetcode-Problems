class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lcs=1
        if len(nums)==0:
            return 0
        numset= set()
        for i in nums:
            numset.add(i)
        for num in numset:
            if num-1 in numset:
                continue
            else:
                count=1
                while (num+count) in numset:
                    count+=1 
                if lcs< count:
                    lcs= count 
        return lcs