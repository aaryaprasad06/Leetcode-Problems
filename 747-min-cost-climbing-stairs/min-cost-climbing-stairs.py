class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n= len(cost)
        memo= [0] * (n+1)
        for i in range(2, n+1):
            v1 = memo[i-1] + cost[i-1]
            v2 = memo[i-2] + cost[i-2]
            memo[i] = min(v1, v2)
        return memo[n]
