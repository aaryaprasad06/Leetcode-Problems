class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result= []
        path= [] 
        nums= [i for i in range(1, n+1)]

        def f(k, idx):
            if len(path)==k:
                result.append(path[:])
                return 
            
            for i in range(idx, len(nums)):
                path.append(nums[i])
                f(k,i+1)
                path.pop()


        f(k, 0)
        return result