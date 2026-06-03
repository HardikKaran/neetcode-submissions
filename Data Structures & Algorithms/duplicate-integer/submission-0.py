class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        unique = sorted(set(nums))
        if unique == sorted(nums):
            return False
        else:
            return True
