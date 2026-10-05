class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        ans= [n for m, n in sorted(zip(heights, names))]
        return ans[::-1]
