class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq= 0
        currsum= 0
        prefix= {0:1}
        for num in nums:
            currsum+= num 
            if currsum-k in prefix:
                freq+= prefix[currsum-k]
            prefix[currsum]= prefix.get(currsum, 0)+1
        return freq