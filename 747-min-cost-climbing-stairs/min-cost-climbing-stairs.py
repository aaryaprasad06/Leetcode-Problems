class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n= len(cost)
        mem= [0]*(n+1)
        for i in range(2, n+1):
            v1= mem[i-1]+cost[i-1]
            v2= mem[i-2]+cost[i-2]
            mem[i]= min(v1, v2)
        return mem[-1]