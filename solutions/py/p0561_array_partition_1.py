class Solution(object):
    def arrayPairSum(self, nums):
        nums = sorted(nums)
        dim = len(nums)
        total = 0
        for q in range (0, dim/2):
            total += nums[2*q]
        return total
