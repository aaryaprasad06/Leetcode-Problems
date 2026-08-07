class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result= []
        path= []
        candidates.sort()
        def f(s, idx):
            if s==target:
                result.append(path[:])
                return 
            if s > target:
                return 
            for i in range(idx, len(candidates)):
                if i>idx and candidates[i]== candidates[i-1]:
                    continue
                path.append(candidates[i])
                s+= candidates[i]
                f(s, i+1)
                s-=candidates[i]
                path.pop()
        
        f(0, 0)
        return result