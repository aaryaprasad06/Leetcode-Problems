class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bs(nums, target):
            low= 0
            high= len(nums)-1
            if target > nums[high]:
                return False
            if len(nums)==2:
                if nums[0]==target or nums[1]==target:
                    return True
                else:
                    return False
            while low<=high:
                mid= (low+high)//2
                if nums[mid]==target:
                    return True
                elif nums[mid] < target:
                    low= mid+1
                else:
                    high= mid-1
        
        for nums in matrix:
            res= bs(nums, target)
            if res==True:
                return True
            
        return False
            