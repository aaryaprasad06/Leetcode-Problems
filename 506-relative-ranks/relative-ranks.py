class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        medals= ["Gold Medal", "Silver Medal", "Bronze Medal"]
        order= sorted(score, reverse= True)
        rank = {s: i for i, s in enumerate(order)}
        return [medals[rank[s]] if rank[s] < 3 else str(rank[s] + 1) for s in score]