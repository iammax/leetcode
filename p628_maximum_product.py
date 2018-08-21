class Solution(object):
    def maximumProduct(self, nums):
        nums = sorted(nums)
        pos = nums[-1] * nums[-2] * nums[-3]
        partial = nums[-1] * nums[0] * nums[1]
        return max(pos, partial)
