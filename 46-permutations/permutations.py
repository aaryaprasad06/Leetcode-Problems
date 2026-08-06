class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result= []
        path= []
        used= set() 

        def f(nums, used):
            if len(path)==len(nums):
                result.append(path[:])
                return 
            
            for num in nums:
                if num in used:
                    continue 
                path.append(num)
                used.add(num)
                f(nums, used)
                path.pop()
                used.remove(num)
        

        f(nums, used)
        return result