class Solution(object):
    def findMin(self, nums):
        themin = nums[0]
        for q in nums[1:]:
            if q < themin:
                return q
        return themin
