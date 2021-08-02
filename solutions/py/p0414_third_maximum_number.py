class Solution(object):
    def thirdMax(self, nums):
        theset = sorted(list(set(nums)))
        try:
            return theset[-3]
        except:
            return theset[-1]
