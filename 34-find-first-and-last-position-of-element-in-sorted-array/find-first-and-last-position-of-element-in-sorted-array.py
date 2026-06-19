class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(nums, target):
            low= 0
            high= len(nums)-1
            while low<=high:
                mid= (low+high)//2
                if nums[mid]<target:
                    low= mid+1
                else:
                    high= mid-1
            return low

        def findRight(nums, target):
            low=0
            high= len(nums)-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid] <= target:
                    low= mid+1
                else:
                    high= mid-1
            return high
        
        left= findLeft(nums, target)
        right= findRight(nums, target)

        if left>right or left==len(nums) or nums[left]!=target:
            return [-1, -1]
        return [left, right]