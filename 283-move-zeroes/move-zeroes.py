class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr=0
        l= len(nums)
        for i in range(l):
            if nums[i]!=0:
                nums[ptr]= nums[i]
                ptr+=1
        while ptr<l:
            nums[ptr]=0
            ptr+=1

        