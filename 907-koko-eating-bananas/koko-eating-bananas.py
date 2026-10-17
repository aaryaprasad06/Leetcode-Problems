class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right= 1, max(piles)
        res= right 
        while left <= right:
            k= (left+right) // 2
            total_hours= sum(math.ceil(pile/k) for pile in piles )
            if total_hours <= h:
                res= k 
                right= k-1 
            else:
                left= k+1 
        return res