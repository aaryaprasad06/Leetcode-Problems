class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result= []
        path= [] 

        def f(s, idx):
            if s==target:
                result.append(path[:])
                return 
            if s>target:
                return 

            while idx<len(candidates):
                path.append(candidates[idx])
                s+= candidates[idx]
                f(s, idx)
                path.pop()
                s-= candidates[idx]
                idx+=1
        
        f(0, 0)
        return result