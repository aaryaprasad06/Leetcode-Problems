class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        seen=[]
        for i in nums:
            if i not in seen:
                seen.append(i)
        if len(seen)<3:
            return max(seen)
            
        for i in range(2):
            maxi= max(seen)
            seen.remove(maxi)
        return max(seen)
