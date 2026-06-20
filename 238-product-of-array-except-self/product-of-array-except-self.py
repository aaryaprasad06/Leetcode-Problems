class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=1
        postfix=1
        ans=[0]*len(nums)

        for i in range(len(nums)):
            ans[i]= prefix
            prefix *= nums[i]
        
        for i in range(len(nums)-2, -1, -1):
            postfix *= nums[i+1]
            ans[i] *= postfix
        return ans