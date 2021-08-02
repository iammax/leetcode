#TODO: Optimize outer loop over q. Shouldn't need to check each case; however it does work

class Solution(object):
    def specialArray(self, nums):
        for q in range (0, 1+max(nums)):
            if len([x for x in nums if x >= q]) == q:
                return q
        return -1
