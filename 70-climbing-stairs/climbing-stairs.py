class Solution:
    def climbStairs(self, n: int) -> int:
        memory={}

        def climb(n):
            if n == 1:
                return 1
            if n ==  2:
                return 2
            if n in memory:
                return memory[n]
            else:
                result = climb(n-1) + climb(n-2)
                memory[n] = result

            return result
        
        return climb(n)