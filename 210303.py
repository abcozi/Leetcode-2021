class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        for i in range(n):
            if nums[i] != i:
                return i
        return n