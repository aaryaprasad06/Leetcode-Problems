class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]==0 and nums[j]!=0:
                    nums[j], nums[i]= nums[i], nums[j]
                    break