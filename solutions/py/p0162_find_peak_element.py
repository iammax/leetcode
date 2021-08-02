class Solution(object):
    def findPeakElement(self, nums):
        dim = len(nums)
        if dim > 2:
            for q in range (1, dim-1):
                if nums[q] > nums[q-1] and nums[q] > nums[q+1]:
                    return q
            return nums.index(max(nums[0], nums[-1]))
        else:
            return nums.index(max(nums))
