class Solution(object):
    def findLengthOfLCIS(self, nums):
        counter = 0
        dim = len(nums)
        best = 0
        if len(nums) == 0:
            return 0
        here = nums[0]
        streak = 1
        while counter < dim-1:
            nextone = nums[counter+1]
            if here < nextone:
                streak += 1
            else:
                if streak > best:
                    best = streak
                streak = 1
            here = nextone
            counter += 1
        return max(best, streak)
