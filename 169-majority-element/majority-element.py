class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority=nums[0]
        votes=1
        for i in range(1, len(nums)):
            if (votes==0):
                votes+=1
                majority= nums[i]
            elif majority==nums[i]:
                votes+=1
            else:
                votes-=1
        return majority
        