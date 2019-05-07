class Solution(object):
    def findDuplicates(self, nums):
        nums = sorted(nums)
        out = []
        dim = len(nums)
        counter = 1
        while counter < dim:
            if nums[counter] == nums[counter-1]:
                out.append(nums[counter])
            counter += 1
        return out
