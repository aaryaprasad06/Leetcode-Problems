class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            complement= target - nums[i]
            if complement in nums and nums.index(complement) !=i:
                ans.append(i)
                ans.append(nums.index(complement))
                return ans