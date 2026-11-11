class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        d= {} 

        for i in range(len(nums)):
            if nums[i] in d:
                return True 
            d[nums[i]]= i 

            if len(d)>k:
                del d[nums[i-k]]
        return False