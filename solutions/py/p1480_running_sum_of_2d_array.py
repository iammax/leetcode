class Solution(object):
    def runningSum(self, nums):
        out = [nums[0]]
        for q in range (1, len(nums)):
            out.append(out[q-1] + nums[q])
        return out
