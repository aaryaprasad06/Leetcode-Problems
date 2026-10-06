class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d= {}
        for i in range(len(nums)):
            complement= target - nums[i] 
            if complement in d:
                return [i, d[complement]]
            else:
                d[nums[i]]= i