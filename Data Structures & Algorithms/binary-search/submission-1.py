class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = round((l + r) / 2)
            # mid = l + ((r - l) // 2) doesnt overflow because r - l will always be less than max index

            if nums[mid] < target:
                l = mid + 1
            
            elif nums[mid] > target: 
                r = mid - 1
            
            elif nums[mid] == target:
                return mid
            
        return -1