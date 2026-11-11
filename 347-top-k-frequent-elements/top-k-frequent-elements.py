from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq= Counter(nums)
        ans= []
        while len(ans)!=k:
            most= max(freq.values()) 
            for key, value in freq.items():
                if value== most:
                    ans.append(key) 
                    del freq[key]
                    break 
        return ans