class Solution:
    def tribonacci(self, n: int) -> int:
        memory= {}

        def helper(n):
            if n == 0: return 0
            if n == 1: return 1
            if n == 2: return 1 

            if n in memory:
                return memory[n]
            else:
                result = helper(n-1) + helper(n-2) + helper(n-3)
                memory[n] = result 
            
            return result 
        
        return helper(n)
