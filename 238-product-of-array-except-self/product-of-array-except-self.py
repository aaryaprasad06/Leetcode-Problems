class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix= 1
        postfix= 1
        product= [0] * len(nums)

        for i in range(len(nums)):
            product[i]= prefix
            prefix*= nums[i]
        
        for i in range(len(nums)-2, -1, -1):
            postfix *= nums[i+1]
            product[i] *= postfix 
        return product
            