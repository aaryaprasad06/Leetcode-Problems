class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result= []
        used= set()
        path= [] 
        nums= [i for i in range(1, n+1)]

        def f(k, used, idx):
            if len(path)==k:
                result.append(path[:])
                return 
            
            for i in range(idx, len(nums)):
                if nums[i] in used:
                    continue
                path.append(nums[i])
                used.add(nums[i])
                f(k, used, i+1)
                path.pop()
                used.remove(nums[i])


        f(k, used, 0)
        return result