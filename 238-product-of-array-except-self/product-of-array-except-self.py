class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix= 1
        postfix= 1
        arr= [1]* len(nums)
        for i in range(1, len(nums)):
            prefix*= nums[i-1]
            arr[i]= prefix 
        for i in range(len(nums)-2, -1, -1):
            postfix*=  nums[i+1]
            arr[i]*= postfix 
        return arr
             