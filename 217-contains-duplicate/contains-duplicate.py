class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        unique= set(nums)
        return not(len(unique)== len(nums))