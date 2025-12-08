class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution=[]
        for i in range(len(nums)):
            complement= target- nums[i]
            if complement in nums and nums.index(complement)!=i:
                pos= nums.index(complement)
                solution= [i, pos]
                break
        return solution