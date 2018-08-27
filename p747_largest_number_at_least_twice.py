class Solution(object):
    def dominantIndex(self, nums):
        if len(nums) == 1:
            return 0
        new = sorted(nums)
        biggest = new[-1]
        second = new[-2]
        if biggest >= second*2:
            return nums.index(biggest)
        else:
            return -1
