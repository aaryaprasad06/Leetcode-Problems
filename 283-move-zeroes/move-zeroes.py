class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n= len(nums)
        last_non_zero=0
        for current in range(n):
            if nums[current]!=0:
                if current !=last_non_zero:
                    nums[last_non_zero]= nums[current]
                    nums[current]= 0
                last_non_zero+=1