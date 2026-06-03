class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        idx = 0

        for val in nums:
            if (target - val) in hashMap:
                return [hashMap[target - val], idx]
            hashMap[val] = idx
            idx += 1