class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq= {}
        for digit in nums:
            freq[digit]= freq.get(digit, 0)+1 
        ans= []
        while len(ans)!= k:
            mostfreq= max(freq.values())
            for key, value in freq.items():
                if value== mostfreq:
                    ans.append(key)
                    del freq[key]
                    break
        return ans

            