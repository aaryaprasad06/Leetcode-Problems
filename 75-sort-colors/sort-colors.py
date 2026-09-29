class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind= 0
        n= len(nums)
        for i in range(n-1):
            min_idx= i
            for j in range(i+1, n):
                if nums[j] < nums[min_idx]:
                    min_idx= j 
            nums[ind], nums[min_idx]= nums[min_idx], nums[ind]
            ind+=1
        return nums