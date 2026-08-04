class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans= [[]]
        curr= []

        def f(nums, idx):
            if idx== len(nums):
                if len(curr) > 0:
                    ans.append(curr.copy())
                return 
            curr.append(nums[idx])
            f(nums, idx+1)
            curr.pop()
            f(nums, idx+1)
        f(nums, 0)
        return ans