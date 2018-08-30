class Solution(object):
    def search(self, nums, target):
        rightbound = len(nums)
        counter = rightbound/2
        leftbound = 0
        prevval = nums[0]
        while True:
            thisval = nums[counter]
            if thisval == target:
                return counter
            elif thisval > target:
                rightbound = counter
            else:
                leftbound = counter
            if prevval == thisval:
                return -1
            prevval = thisval
            counter = (leftbound + rightbound)/2
        return -1
